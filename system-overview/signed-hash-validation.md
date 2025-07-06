# Signed Hash Validation

Signed Hash Validation provides end users with a way to verify that a VotingWorks machine is running authentic unmodified VotingWorks software.

The machine preps a payload consisting of the following, with `1//shv1//` as a prefix and `#` as a separator:

* System hash
* Software version
* Election ID
* Current timestamp

The machine signs that payload with its TPM private key and then bundles the following together, with `;` as a separator:

* Payload
* Payload signature
* Machine cert

This combination is displayed as a QR code. Putting this all together, the QR code contains:

```
message = 1//shv1//<system-hash>#<software-version>#<election-id>#<current-timestamp>
qrCode  = <message>;signature(<message>);<machine-cert>
```

This QR code can be scanned at [https://check.voting.works](https://check.voting.works). The site parses the QR code and performs the following verification:

* Verifies the machine cert using the root VotingWorks cert.
* Extracts the machine's public key from the machine cert.
* Uses that public key to verify the payload signature against the original payload. If this verification succeeds, we can be confident that the machine possesses the TPM private key that pairs with the public key in the machine cert.
* Because the TPM private key will only sign data if the system hash is correct, per [system-integrity.md](../system-security-auditing-and-logging/system-security-architecture/system-integrity.md "mention"), we can further be confident that the software on the machine is authentic and unmodified.

After completing the above verification, [https://check.voting.works](https://check.voting.works) displays a success indicator alongside the payload components and the machine ID as extracted from the machine cert. These attributes can be matched against what's displayed on the machine.

|                                 Machine UX                                 |                                 Web UX                                 |
| :------------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="../.gitbook/assets/machine (1).png" alt="" data-size="original"> | <img src="../.gitbook/assets/web (2).PNG" alt="" data-size="original"> |

## QR Code Specifications

Signed Hash Validation QR codes are [Model 2 QR codes](https://www.qrcode.com/en/codes/model12.html) with [Level H error correction](https://www.qrcode.com/en/about/error_correction.html).

## Code Links

Refer to the following code links for more details:

* [https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/signed\_hash\_validation.ts](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/auth/src/signed_hash_validation.ts)
