# Secure Boot Signing

To finalize an image for production use, it's necessary to sign the image with the VotingWorks Secure Boot keys so that the image can be used on a Secure-Boot-enabled machine. This process requires the use of sensitive keys and a passphrase that should only ever be known to and used by VotingWorks. Since the Trusted Build process is performed by a third-party vendor (SLI), a process to securely sign the image without compromising the keys or passphrase is needed. This document describes that process.

## Transferring an Unsigned Image from SLI to VotingWorks

Once SLI has created a Trusted Build image, the image and its VM definition (an XML file) must be securely provided to VotingWorks. To transfer the image and definition, SLI will upload to a shared S3 bucket only accessible to SLI and VotingWorks. This access is controlled via IAM permission policies.

NOTE: For documentation purposes, we will use a Trusted Build image named **vxadmin**. Replace that with the appropriate image name, as necessary.

Once SLI has configured their S3 access and created a Trusted Build image, they will need to upload the image and its configuration file. Additionally, hashes of each file will be generated so that SLI and VotingWorks can confirm files were not modified during the upload or download phases.

On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-unsigned-upload.sh vxadmin
```

Once the SLI upload has completed, VotingWorks will download and verify the hash values of all files. On the VotingWorks secure build machine, while SLI observes:

```
sudo /home/vx/code/vxsuite-build-system/scripts/sb-unsigned-download.sh vxadmin
```

Once the VotingWorks download has completed and been verified, and the VM has been successfully defined, VotingWorks can proceed with its Secure Boot signing process, while SLI observes.

## Secure Boot Signing

VotingWorks will boot the VM, attach a virtual device containing our Secure Boot signing keys, and select the option to "Lock the System Down" from the vendor menu. When prompted, VotingWorks will enter the passphrase for the Secure Boot signing keys.

When the process completes, the lock-down script displays the system hash. This hash will be provided to SLI/EAC for official verification of the image.

## Transferring a Signed Image from VotingWorks to SLI

Now that the image has been securely signed, VotingWorks will upload the signed image for SLI to later download. While SLI observes, VotingWorks will run the following command on the VotingWorks secure build machine:

```
sudo /home/vx/code/vxsuite-build-system/scripts/sb-signed-upload.sh vxadmin
```

Once this step has completed, SLI can download the files at their convenience. On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-signed-download.sh vxadmin
```

Once SLI has completed the download, and hashes have been validated, the compressed image and signature can be provided to EAC for official use. At any point after submission to EAC, election officials and VotingWorks can verify the image hash via Secure Hash Validation, the vendor menu, or the vx-verifier tool.
