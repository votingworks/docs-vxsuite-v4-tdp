# Verifying the Image Installed on a Machine

## Signed Hash Validation

Once a machine has been imaged with a signed image, you can verify the system hash against the hash of what was built and signed during the Trusted Build process. To perform this verification, VotingWorks provides Signed Hash Validation.

See [Signed Hash Validation](../../system-overview/signed-hash-validation.md) for details.

Note: On older releases (v4.0.1 and earlier), the Secure Boot signing process only output a SHA256 hash value. That hash value needs to be converted to a base64 encoded value to match what is provided by Signed Hash Validation. That can be accomplished with the following command:

```
echo HASH | xxd -r -p | base64
```

## vx-iso

The system hash can also be computed from outside the application, using a vx-iso USB drive as described under [preparing-usb-drives-for-imaging.md](preparing-usb-drives-for-imaging.md "mention"). After booting from the drive, simply select the option to "Compute System Hash".
