# Verifying the Image Installed on a Machine

Once a machine has been imaged with a signed image, you can verify the system hash against the hash of what was built and signed during the Trusted Build process. To perform this verification, VotingWorks provides Signed Hash Validation.

See [Signed Hash Validation](../../system-overview/signed-hash-validation.md) for details.

Note: In some releases (v4.0.1 and earlier), the Secure Boot signing process only output a SHA256 hash value. That hash value needs to be converted to a base64 encoded value to match what is provided by Signed Hash Validation. That can be accomplished with the following command:

```
echo HASH | xxd -r -p | base64
```



[\
](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/installing-an-image-via-vx-iso/machine-configuration-wizard-and-vxcertifier)
