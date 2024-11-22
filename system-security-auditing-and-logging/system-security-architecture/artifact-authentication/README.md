# Artifact Authentication

When a VxSuite machine exports data to a USB for another VxSuite machine to import, the first machine digitally signs that data so that the second machine can verify its authenticity. We use this mechanism in two places in particular:

1. To authenticate “ballot packages” — These configuration bundles are exported by VxAdmin and used to configure VxCentralScan and VxScan.
2. To authenticate cast vote records — These are exported by VxCentralScan and VxScan and imported by VxAdmin for tabulation.

The exporting machine digitally signs the following message using its TPM private key:

`MESSAGE_FORMAT_VERSION + “//” + ARTIFACT_TYPE + “//” + ARTIFACT_CONTENTS`

It then outputs the following to a .vxsig file:

`SIGNATURE_LENGTH + SIGNATURE + SIGNING_MACHINE_CERTIFICATE`

The importing machine parses the above, extracts the exporting/signing machine’s public key from its certificate as provided in the .vxsig file, reconstructs the message, and then verifies the signature. The importing machine also importantly verifies that the signing machine certificate in the .vxsig file is a valid certificate that is 1) signed by VotingWorks and 2) for the expected machine given the artifact type, e.g. VxAdmin if the artifact is a ballot package. We verify 1 using the VotingWorks CA certificate installed on every machine.

If signature verification fails on the importing machine, the importing machine will refuse to import the artifact. This provides protection against data tampering and/or corruption as data is transferred from one machine to another via USB.

### Code Links

Refer to the following codebase links for more detail on VxSuite artfiact authentication:

* [https://github.com/votingworks/vxsuite/tree/main/libs/auth](https://github.com/votingworks/vxsuite/tree/main/libs/auth) — VxSuite authentication lib, a good starting point for all things authentication
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/artifact\_authenticator.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/artifact\_authenticator.ts) —  Artifact authentication logic
* [https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/cryptography.ts](https://github.com/votingworks/vxsuite/blob/main/libs/auth/src/cryptography.ts) — OpenSSL commands underlying various authentication and signing operations
