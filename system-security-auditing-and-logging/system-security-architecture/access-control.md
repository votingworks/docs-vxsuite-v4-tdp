# Access Control

## Certification of VxSuite Components

VxSuite is composed of individual machines, namely VxAdmin, VxCentralScan, VxMarkScan, and VxScan, as well as smart cards for authentication. Each machine and each smart card has a unique 256-bit ECC private key (or keys in the case of smart cards) stored in tamper-resistant hardware, plus one or more X.509 certificates for the corresponding public key (or keys) with relevant attributes bound.

This means that every VxSuite component can prove its authenticity, notably to any other VxSuite component. For example, a smart card can prove to a VxAdmin that it is a valid election administrator card for a particular election, or a VxScan can export digitally signed cast vote records, which a VxAdmin can then verify are authentic before importing.

Certification relationships work as follows:

* VotingWorks directly certifies the type of every component, i.e., VxAdmin machine, VxCentralScan machine, VxMarkScan machine, VxScan machine, or smart card. This makes it such that only components that are “blessed” by VotingWorks can successfully communicate with each other. This is also important for defense-in-depth and separation of privileges, as one VotingWorks component type cannot act like another, e.g., a VxScan cannot sign an election configuration package like a VxAdmin can. Because machine certificates include a machine ID, it's also the case that, say, VxScan SC01 cannot sign CVRs as VxScan SC02.
* VotingWorks further certifies every VxAdmin as bound to a particular jurisdiction, e.g., Warren County, Mississippi. This is important because VxAdmins program smart cards and should not be able to program cards for other jurisdictions.
* Every smart card, in addition to being certified directly by VotingWorks, is certified by a VxAdmin during card programming. A card’s VxAdmin-issued certificate indicates 1) the jurisdiction that the card is bound to, 2) which user role the card has been programmed for, i.e. system administrator card, election manager card, or poll worker card, and 3) in the case of election manager and poll worker cards, the specific election that the card is bound to.

As a diagram:

<figure><img src="../../.gitbook/assets/security-diagram (1).png" alt=""><figcaption></figcaption></figure>

VxCentralScan, VxMarkScan, and VxScan, unlike VxAdmin, aren’t bound to a jurisdiction by VotingWorks. They’re bound and unbound to jurisdictions as they’re configured and unconfigured by election managers. When an election manager configures a VxCentralScan, VxMarkScan, or VxScan for an election, the machine persists in its datastore the jurisdiction of the election manager card used to unlock it and then only accepts cards from that jurisdiction. When the machine is unconfigured for that election, the machine returns to a jurisdiction-agnostic state. This allows one jurisdiction to lend its unconfigured equipment to another, without giving a jurisdiction any power over machines configured for a different jurisdiction.

## Smart Card Keys and Certificates

As described above, programmed smart cards have two certificates, one issued by VotingWorks and one issued by VxAdmin. We generate two key pairs on the card, one for each certificate. We could have chosen to certify the same key twice, but as will be described below, we wanted to have different usage policies for the two private keys, thus the issuance of certificates against two different keys. Smart cards also have PINs (with the exception of poll worker cards, unless an election official chooses to enable poll worker card PINs). These interface as follows:

* The private key slot associated with the card’s VotingWorks-issued certificate is not PIN-gated, so anyone can immediately verify that a card is a VotingWorks-certified card.
* The private key slot associated with the card’s VxAdmin-issued certificate is PIN-gated, so authentication requires PIN entry.
* The card’s VxAdmin-issued certificate, on the other hand, is not PIN-gated, so it’s possible for a VotingWorks machine to know the card’s type and which election it’s bound to even before a PIN is entered. This allows the machine to display error messages like “election mismatch” immediately after card insertion and before PIN entry.
  * This does mean that an attacker could load a fake certificate onto a card such that the machine, at worst, displays an incorrect error message, but nothing more. Authentication would still fail as the public key in the certificate would not match the private key on the card. We take care not to fully trust the information in this certificate until we complete authentication.

We’ve taken inspiration from the NIST Personal Identity Verification (PIV) standard but haven’t strictly adhered to it. Our use case differs from the PIV standard in a number of ways, most notably in that cards are certified by two entities (VotingWorks and VxSuite), rather than just one. We also don’t need VxSuite smart cards to be interoperable with other PIV systems.

The recommended access control policy by role for system administrator, election manager, and poll worker cards is documented in the user manual ([Smart Cards and User Roles](https://docs.voting.works/vxsuite-user-manual-v4/vxadmin-system-setup/programming-cards)). Deviating from this recommended access control policy can result in a violation of the principle of least privilege and users gaining access to voting system functionality that is not intended for them. For example, a poll worker could have access to unconfiguring a voting machine if provided a smart card programmed for a different role.

### Vendor Cards

There's one additional card type, the vendor card, and it differs slightly in its cert structure from the other card types. VotingWorks uses vendor cards to access the vendor menu on machines, for low-level operations like machine key rotation. Vendor cards are programmed directly by VotingWorks and not by VxAdmin. Because of this, vendor cards do not have a VxAdmin-issued cert, but rather, a second VotingWorks-issued cert. The general term that we use for this second cert across all card types is the identity cert, as it confers user role, i.e., identity.

Vendor cards can be programmed to be either jurisdiction-specific or jurisdiction-agnostic.

### Private Key Storage

We store our root VotingWorks certificate authority (CA) private key encrypted in a password vault, usable only by a few authorized engineers.

VxAdmin, VxCentralScan, VxMarkScan, and VxScan are all built on devices with a Trusted Platform Module (TPM) 2.0, a chip that ships standard on modern Intel and AMD hardware. The TPM can keep cryptographic material secret inside its tamper-resistant boundary until a certain set of system conditions are met. Only once the TPM determines that the system meets a set of appropriate conditions—correct bootloader, kernel, kernel command line, etc.—does the TPM allow an application to ask it to perform signing operations with its contained secret key.

Our smart cards are JCOP 4 Java Cards, version 3.0.5. These Java Cards can generate 256-bit ECC key pairs such that the private key never leaves the card, while the public key is exported. The cards are capable of self-destructing if someone attempts to extract the private key at the hardware level.

### Smart Card PINs

Vendor cards, system administrator cards, and election manager cards always have PINs. Poll worker cards do not have PINs by default but can if the system administrator enables them.

PINs are auto-generated random 6-digit numbers, guaranteed not to be weak (e.g. not 11111, 123456, 121212).

After 5 incorrect PIN attempts, users have to wait 15 seconds before they can try again. For every incorrect PIN attempt after that, the wait time doubles (15 seconds → 30 seconds → 60 seconds and so on). After 15 incorrect PIN attempts, the card is completely locked and has to be reprogrammed. System administrators can adjust the number of incorrect PIN attempts allowed without lockout as well as the starting lockout duration. The number of incorrect PIN attempts is stored on the card in a tamper-resistant location (as opposed to on the machine), meaning that taking a card to another machine to gain extra attempts will not work. Removing and reinserting a card restarts the lockout timer.

### Certificate Format

The certificates that we use are effectively vouchers—a certificate authority (CA) vouches that a public key has certain properties, for example that it is the public key of an election manager card for a particular election. This vouching is done by signing data containing the public key and those properties. We use X.509 certificates as they are broadly used and well supported.

While we could use existing X.509 fields like Organization, Organizational Unit, and Serial Number, and wedge our data into those types, overloading existing fields that don’t quite match isn’t ideal and could lead to security issues from type confusion.

Instead, we use our own fields. We’ve registered with IANA to have a VotingWorks enterprise object identifier (OID), which is effectively a prefix for OIDs of the form 1.3.6.1.4.1.32473.123, where 1.3.6.1.4.1.32473 is the enterprise OID for an example organization, and 123 is the 123rd field defined by that organization.

Our IANA-assigned Private Enterprise Number (PEN) is 59817, which means that the enterprise OID, fully-prefixed, is 1.3.6.1.4.1.59817. See [https://www.iana.org/assignments/enterprise-numbers/?q=59817](https://www.iana.org/assignments/enterprise-numbers/?q=59817).

Our custom fields are:

* 1.3.6.1.4.1.59817.1 — Component = admin, central-scan, mark-scan, scan, or card (the first four referring to machines)
* 1.3.6.1.4.1.59817.2 — Jurisdiction = {state-2-letter-abbreviation}.{county-or-town} (e.g., ms.warren or ca.los-angeles)
* 1.3.6.1.4.1.59817.3 — Card type = vendor, system-administrator, election-manager, poll-worker, or poll-worker-with-pin (vendor, system administrator, and election manager cards always have PINs)
* 1.3.6.1.4.1.59817.4 — Election ID = The ID of the election that an election card was programmed for\*
* 1.3.6.1.4.1.59817.5 — Election date = The date of the election that an election card was programmed for
* 1.3.6.1.4.1.59817.6 — Machine ID = A VxAdmin, VxCentralScan, VxMarkScan, or VxScan machine ID

\*This is not the same election ID as displayed in machine footers. The election ID as it pertains to cards is the `id` field in the election definition. The election ID as it pertains to machine footers is actually a hash, specifically `<first-7-digits-of-hash-of-election-json>-<first-7-digits-of-hash-of-election-zip>`. The reason for not using the latter in card certificates is to avoid having to reprogram cards after election package edits for what is conceptually still the same election.

## Certificate Expiries

X.509 certificates eventually expire. We use the following expiry times:

* Certificates directly issued by VotingWorks: 100 years
* VxAdmin-issued system administrator card certificates: 5 years
* VxAdmin-issued election manager and poll worker card certificates: 6 months
* VotingWorks-issued vendor card certificates: 7 days

This means that system administrator cards will automatically expire after 5 years, election manager and poll worker cards will automatically expire after 6 months, and vendor cards will automatically expire after 7 days.

## Configuration and Authentication Process

### Configuration at VotingWorks Facility

Configuration of VxSuite components begins at a secure VotingWorks facility. At this facility is a VotingWorks certification terminal, VxCertifier. VxCertifier is a fully offline air-gapped terminal with access to the root VotingWorks private key.

Using VxCertifier, VotingWorks prepares and certifies smart cards for use with VotingWorks machines:

1. VotingWorks installs the appropriate security module code on the card.
2. VotingWorks instructs the smart card to generate a key pair and export the public key.
3. The root VotingWorks CA certifies the card public key and saves the resulting certificate onto the card.

The card is now VotingWorks-certified but “blank” from the perspective of VotingWorks machines.

VotingWorks also certifies its machines at this facility. After a machine has been imaged with our latest software release, the machine boots into a configuration wizard. The software image includes the root VotingWorks CA certificate, so no extra work is required beyond imaging to “install” that certificate. Using the configuration wizard and VxCertifier, VotingWorks certifies machines:

1. VotingWorks machine code instructs the machine’s TPM to generate a key pair and export the public key.
2. VotingWorks machine code generates a certificate signing request (CSR) for that public key and writes the CSR to a USB drive.
   1. On VxAdmin, VotingWorks additionally specifies a jurisdiction. That jurisdiction is included in the CSR.
3. The USB is plugged into VxCertifier. Through VxCertifier, the root VotingWorks CA certifies the machine public key and saves the resulting certificate onto the USB drive.
   1. VxAdmin certificates are themselves CA certificates capable of creating additional certificates (necessary for smart card programming).
4. The USB drive is plugged back into the machine to be certified. The machine loads the certificate from the USB drive, verifies its correctness, and saves it onto its hard drive.
5. On VxAdmin, the configuration wizard also surfaces a prompt to program a first system administrator card to bootstrap the jurisdiction as, from here on out, the machine will need to be unlocked by a system administrator card in order to program any other cards.

Machines, a first system administrator card, and “blank” cards are shipped to jurisdictions.

### Smart Card Programming

In the field, election officials use their VxAdmin and their first system administrator card to program additional smart cards. Smart card programming involves the following steps:

1. VxAdmin retrieves the card’s VotingWorks-issued certificate and verifies that it was signed by VotingWorks using the VotingWorks CA certificate installed on every machine.
2. VxAdmin resets the card PIN, which further causes the card to clear all of its PIN-gated key slots, essentially unprogramming it if it was previously programmed.
3. VxAdmin instructs the card to generate a key pair and export the public key. This key pair is distinct from the key pair that VotingWorks generated.
4. The VxAdmin CA certifies the card public key, assigning relevant attributes like the jurisdiction, card type, and election if applicable, and saves the resulting certificate to the card.
5. VxAdmin also saves its own CA certificate onto the card (more on how this is used under Authentication).

### Authentication

Smart card authentication involves the following steps:

1. The machine retrieves the card’s VotingWorks-issued certificate and verifies that it was signed by VotingWorks using the VotingWorks CA certificate installed on every machine.
2. The machine retrieves 1) the card’s VxAdmin-issued certificate and 2) the certificate of the VxAdmin that programmed the card, which as noted in [Smart Card Programming](access-control.md#smart-card-programming) is also loaded onto the card. The machine verifies that the former (1) was signed by the latter (2). The machine also verifies that the latter is a valid VxAdmin certificate signed by VotingWorks using the VotingWorks CA certificate, establishing a chain of trust all the way up to a trusted root.
3. The machine verifies that the card has a private key that corresponds to the public key in the card’s VotingWorks-issued certificate by asking the card to sign a challenge with its private key and attempting to verify it with the public key.
4. The machine verifies that the card has a private key that corresponds to the public key in the card’s VxAdmin-issued certificate by asking the card to sign a challenge with its private key and attempting to verify it with the public key.
   1. If the card has a PIN, the card will only proceed with this signature if provided the appropriate PIN. The VotingWorks machine thus asks the user for their PIN to perform this operation.
5. Throughout this process, the machine verifies that certificate fields are valid and consistent. It also verifies that the card jurisdiction and election match the machine jurisdiction and election, where relevant.

### Session Time Limits

Machines automatically lock after they’ve been left idle for 30 minutes and also automatically lock after 12 hours, even if the user has been active. The user is given appropriate heads up. System administrators can select shorter time limits.

These time limits do not apply to unauthenticated screens like the “Insert Your Ballot” screen on VxScan.

### Code Links

Refer to the following code links for more details:

* [https://github.com/votingworks/vxsuite/tree/v4.0.2/libs/auth](https://github.com/votingworks/vxsuite/tree/v4.0.2/libs/auth) — VxSuite authentication lib, a good starting point for all things authentication
* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/dipped\_smart\_card\_auth.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/dipped_smart_card_auth.ts) — High-level authentication state management for VxAdmin and VxCentralScan
* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/inserted\_smart\_card\_auth.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/inserted_smart_card_auth.ts) — High-level authentication state management for VxScan
* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/java\_card.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/java_card.ts) — Java Card implementation
* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/certs.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/certs.ts) — Certificate configuration
* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/cryptography.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/cryptography.ts) — OpenSSL commands underlying various authentication and signing operations
* [https://github.com/votingworks/vxsuite-complete-system/blob/v4.0.2/config/vendor-functions/basic-configuration.sh](https://github.com/votingworks/vxsuite-complete-system/blob/v4.0.2/config/vendor-functions/basic-configuration.sh) — The production machine configuration wizard
* [https://github.com/votingworks/vxsuite/tree/v4.0.2/libs/auth#scripts](https://github.com/votingworks/vxsuite/tree/v4.0.2/libs/auth#scripts) — A summary of the scripts in the authentication lib, many of which are used for production configuration
* [https://github.com/votingworks/openfips201](https://github.com/votingworks/openfips201) — The applet that we’re installing onto our Java Cards



















