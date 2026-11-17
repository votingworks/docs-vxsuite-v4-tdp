# Verifying the Image Installed on a Machine

## Signed Hash Validation

Once a machine has been imaged with a signed image, its system hash can be verified against the hash of what was built and signed during the Trusted Build process. To perform this verification, VotingWorks provides Signed Hash Validation.

See [Signed Hash Validation](../../system-overview/signed-hash-validation.md) for details.

{% hint style="info" %}
On older releases (v4.0.1 and earlier), the Secure Boot signing process only output a SHA256 hash value. That hash value must be converted to a base64-encoded value to match what Signed Hash Validation provides. To convert it, run the following command, replacing `HASH` with the SHA256 hash value:

```
echo HASH | xxd -r -p | base64
```
{% endhint %}

## vx-iso

The system hash can also be computed from outside the application, using a vx-iso USB drive as described under [preparing-usb-drives-for-imaging.md](preparing-usb-drives-for-imaging.md "mention"). To compute the system hash with vx-iso:

1. Connect the vx-iso USB drive to a machine after the machine has been successfully imaged with the target software image.
2. Power the machine on. The machine boots automatically from the vx-iso USB drive.
3. If the machine in question does not have a keyboard, connect a keyboard.
4. Select the option to `Compute System Hash`. This runs an open-source script that itself uses standard, non-proprietary, open-source tools to compute a system hash. The script source code is available publicly as [compute-system-hash.sh in the vx-iso repository](https://github.com/votingworks/vx-iso/blob/main/live-build/includes.chroot/usr/local/bin/compute-system-hash.sh). A snapshot of the script source code has also been included for the test lab under `software-docs/compute-system-hash.sh`.
5. The hash is displayed in base64 format. Check this hash against the hash published by the U.S. Election Assistance Commission (EAC) for the target software image.
