# Access Control

## Certification of VxSuite Components

VxSuite is composed of individual machines, namely VxAdmin, VxCentralScan, and VxScan, as well as smartcards for authentication. Each machine and each smartcard has a unique 256-bit ECC private key (or keys in the case of smart cards) stored in tamper-resistant hardware, plus one or more X.509 certificates for the corresponding public key (or keys) with relevant attributes bound.

This means that every VxSuite component can prove its authenticity, notably to any other VxSuite component. For example, a smartcard can prove to a VxAdmin that it is a valid election administrator card for a particular election, or a VxScan can export digitally signed cast vote records, which a VxAdmin can then verify are authentic before importing.

Certification relationships work as follows:

* VotingWorks directly certifies the type of every component, i.e. VxAdmin machine, VxCentralScan machine, VxScan machine, or smartcard. This makes it such that only components that are “blessed” by VotingWorks can successfully communicate with each other. This is also important for defense-in-depth as one VotingWorks component type cannot act like another, e.g. a VxScan cannot sign an election configuration package like a VxAdmin can.
* VotingWorks further certifies every VxAdmin as bound to a particular jurisdiction, e.g. Warren County, Mississippi. This is important because VxAdmins program smartcards and should not be able to program cards for other jurisdictions.
* Every smartcard, in addition to being certified directly by VotingWorks, is certified by a VxAdmin during card programming. A card’s VxAdmin-issued certificate indicates 1) the jurisdiction that the card is bound to, 2) which user role the card has been programmed for, i.e. system administrator card, election manager card, or poll worker card, and 3) in the case of election manager and poll worker cards, the specific election that the card is bound to.

As a diagram:

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

VxCentralScan and VxScan, unlike VxAdmin, aren’t bound to a jurisdiction by VotingWorks. They’re bound and unbound to jurisdictions as they’re configured and unconfigured by election managers. When an Election Manager configures a VxCentralScan or VxScan for an election, the machine persists in its datastore the jurisdiction of the Election Manager card used to unlock it and then only accepts cards from that jurisdiction. When the machine is unconfigured for that election, the machine returns to a jurisdiction-agnostic state.

## Smartcard Keys and Certificates

As described above, programmed smartcards have two certificates, one issued by VotingWorks and one issued by VxAdmin. We generate two key pairs on the card, one for each certificate—we don’t certify the same card public key twice. Smart cards also have PINs (with the exception of poll worker cards, unless an election official chooses to enable poll worker card PINs). These interface as follows:

* The private key slot associated with the card’s VotingWorks-issued certificate is not PIN-gated, so anyone can verify that a card is a VotingWorks-certified card.
* The private key slot associated with the card’s VxAdmin-issued certificate is PIN-gated, so authentication requires PIN entry.
* The card’s VxAdmin-issued certificate, on the other hand, is not PIN-gated, so it’s possible for a VotingWorks machine to know the card’s type and which election it’s bound to even before a PIN is entered. This allows the machine to display error messages like “election mismatch” immediately after card insertion and before PIN entry.
  * This does mean that an attacker could load a fake certificate onto a card such that the machine, at worst, displays an incorrect error message, but nothing more. Authentication would still fail as the public key in the certificate would not match the private key on the card. We take care not to fully trust the information in this certificate until we complete authentication.

We’ve taken inspiration from the NIST Personal Identity Verification (PIV) standard but haven’t strictly adhered to it. Our use case differs from the PIV standard in a number of ways, most notably in that cards are certified by two entities (VotingWorks and VxSuite), rather than just one. We also don’t need VxSuite smartcards to be interoperable with other PIV systems.

### Private Key Storage

We store our root VotingWorks certificate authority (CA) private key encrypted in a password vault, usable only by a few authorized engineers.

VxAdmin, VxCentralScan, and VxScan are all built on devices with a Trusted Platform Module (TPM) 2.0, a chip that ships standard on modern Intel and AMD hardware. The TPM can keep cryptographic material secret inside its tamper-resistant boundary until a certain set of system conditions are met. Only once the TPM determines that the system meets a set of appropriate conditions—correct bootloader, kernel, kernel command line, etc.—does the TPM allow an application to ask it to perform signing operations with its contained secret key.

Our smart cards are Java Cards, version 3.0.4. These Java Cards can generate 256-bit ECC key pairs such that the private key never leaves the card, while the public key is exported. The cards are capable of self-destructing if someone attempts to extract the private key at the hardware level.

### Smart Card PINs

System administrator cards and election manager cards always have PINs. Poll worker cards do not have PINs by default but can if the system administrator enables them.

PINs are auto-generated random 6-digit numbers, guaranteed not to be weak (e.g. not 11111, 123456, 121212).

After 5 incorrect PIN attempts, users have to wait 15 seconds before they can try again. For every incorrect PIN attempt after that, the wait time doubles (15 seconds → 30 seconds → 60 seconds and so on). After 15 incorrect PIN attempts, the card is completely locked and has to be reprogrammed. System administrators can adjust the number of incorrect PIN attempts allowed without lockout as well as the starting lockout duration. The number of incorrect PIN attempts is stored on the card in a tamper-resistant location (as opposed to on the machine), meaning that taking a card to another machine to gain extra attempts will not work. Removing and reinserting a card restarts the lockout timer.

### Certificate Format

The certificates that we use are effectively vouchers—a certificate authority (CA) vouches that a public key has certain properties, for example that it is the public key of an election manager card for a particular election. This vouching is done by signing data containing the public key and those properties. We use X.509 certificates as they are broadly used and well supported.

While we could use existing X.509 fields like Organization, Organizational Unit, and Serial Number, and wedge our data into those types, overloading existing fields that don’t quite match isn’t ideal and could lead to security issues from type confusion.

Instead, we use our own fields. We’ve registered with IANA to have a VotingWorks enterprise object identifier (OID), which is effectively a prefix for OIDs of the form 1.3.6.1.4.1.32473.123, where 1.3.6.1.4.1.32473 is the enterprise OID for an example organization, and 123 is the 123rd field defined by that organization.

Our IANA-assigned Private Enterprise Number (PEN) is 59817, which means that the enterprise OID, fully-prefixed, is 1.3.6.1.4.1.59817. See [https://www.iana.org/assignments/enterprise-numbers/?q=59817](https://www.iana.org/assignments/enterprise-numbers/?q=59817).

Our custom fields are:

* 1.3.6.1.4.1.59817.1 — Component = admin, central-scan, scan, or card (the first three referring to machines)
* 1.3.6.1.4.1.59817.2 — Jurisdiction = {state-2-letter-abbreviation}.{county-or-town} (e.g. ms.warren or ca.los-angeles)
* 1.3.6.1.4.1.59817.3 — Card type = system-administrator, election-manager, poll-worker, or poll-worker-with-pin (system administrator and election manager cards always have PINs)
* 1.3.6.1.4.1.59817.4 — Election hash = The SHA-256 hash of the election definition

## Certificate Expiries

X.509 certificates eventually expire. We use the following expiry times:

* Certificates directly issued by VotingWorks: 100 years
* VxAdmin-issued system administrator card certificates: 5 years
* VxAdmin-issued election manager and poll worker card certificates: 6 months

This means that a system administrator card will automatically expire after 5 years, and election manager and poll worker cards will automatically expire after 6 months.

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
2. VotingWorks machine code generates a certificate signing request (CSR) for that public key and writes the CSR to a USB.
   1. On VxAdmin, VotingWorks additionally specifies a jurisdiction. That jurisdiction is included in the CSR.
3. The USB is plugged into VxCertifier. Through VxCertifier, the root VotingWorks CA certifies the machine public key and saves the resulting certificate onto the USB.
   1. VxAdmin certificates are themselves CA certificates capable of creating additional certificates (necessary for smart card programming).
4. The USB is plugged back into the machine to be certified. The machine loads the certificate from the USB and saves it onto its hard drive.
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
2. The machine retrieves 1) the card’s VxAdmin-issued certificate and 2) the certificate of the VxAdmin that programmed the card, which as noted in [Smart Card Programming](https://docs.google.com/document/d/17qLbrHYkjlEtXx18Oh1TovZz1D1dQd3Ze7azknqd3jA/edit#heading=h.9lruswcmd5zl) is also loaded onto the card. The machine verifies that the former (1) was signed by the latter (2). The machine also verifies that the latter is a valid VxAdmin certificate signed by VotingWorks using the VotingWorks CA certificate, establishing a chain of trust all the way up to a trusted root.
3. The machine verifies that the card has a private key that corresponds to the public key in the card’s VotingWorks-issued certificate by asking the card to sign a challenge with its private key and attempting to verify it with the public key.
4. The machine verifies that the card has a private key that corresponds to the public key in the card’s VxAdmin-issued certificate by asking the card to sign a challenge with its private key and attempting to verify it with the public key.
   1. If the card has a PIN, the card will only proceed with this signature if provided the appropriate PIN. The VotingWorks machine thus asks the user for their PIN to perform this operation.
5. Throughout this process, the machine verifies that certificate fields are valid and consistent. It also verifies that the card jurisdiction and election match the machine jurisdiction and election, where relevant.

### Session Time Limits

Machines automatically lock after they’ve been left idle for 30 minutes and also automatically lock after 12 hours, even if the user has been active. The user is given appropriate heads up. System administrators can select shorter time limits.

These time limits do not apply to unauthenticated screens like the “Insert Your Ballot” screen on VxScan.

### Code Links

Refer to the following codebase links for more detail on VxSuite access control:

* [https://github.com/votingworks/vxsuite/tree/main/libs/auth](https://github.com/votingworks/vxsuite/tree/main/libs/auth) — VxSuite authentication lib, a good starting point for all things authentication
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/dipped\_smart\_card\_auth.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/dipped\_smart\_card\_auth.ts) — High-level authentication state management for VxAdmin and VxCentralScan
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/inserted\_smart\_card\_auth.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/inserted\_smart\_card\_auth.ts) — High-level authentication state management for VxScan
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/java\_card.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/java\_card.ts) — Java Card implementation
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/certs.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/certs.ts) — Certificate configuration
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/cryptography.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/cryptography.ts) — OpenSSL commands underlying various authentication and signing operations
* [https://github.com/votingworks/vxsuite-complete-system/blob/main/config/admin-functions/basic-configuration.sh](https://github.com/votingworks/vxsuite-complete-system/blob/main/config/admin-functions/basic-configuration.sh) — The production machine configuration wizard
* [https://github.com/votingworks/vxsuite/tree/main/libs/auth#scripts](https://github.com/votingworks/vxsuite/tree/main/libs/auth#scripts) — A summary of the scripts in [https://github.com/votingworks/vxsuite/tree/main/libs/auth/scripts](https://github.com/votingworks/vxsuite/tree/main/libs/auth/scripts), many of which are used for production configuration
* [https://github.com/votingworks/openfips201](https://github.com/votingworks/openfips201) — The applet that we’re installing onto our Java Cards


















