# Verifying the Image Installed on a Machine

Once a machine has been imaged with a signed image, you can verify the system hash against the hash of what was built and signed during the Trusted Build process. To perform this verification, you have two options.

### Using vx-verifier

This approach allows you to verify the system hash using a tool outside the system itself. vx-verifier is a modified version of vx-iso.

1. Power the machine down.
2. Insert the vx-verifier USB drive.
3. Power the machine on. It should auto-boot to the vx-verifier USB drive.
4. Navigate to the "Verify Hash" option, attaching a keyboard if necessary.
5. This will calculate and output the system hash of the installed image, which can be checked against the system hash recorded during the Trusted Build process.
6. Once you have verified the hash, you can press "enter" to reboot and remove the vx-verifier USB drive.

### Using Signed Hash Validation

This approach allows you to verify the system hash from within the system. See \[insert link].

[\
](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/installing-an-image-via-vx-iso/machine-configuration-wizard-and-vxcertifier)
