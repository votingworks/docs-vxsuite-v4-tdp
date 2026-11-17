# Secure Boot Signing

To finalize an image for production use, it is necessary to sign the image with the VotingWorks Secure Boot keys so that the image can be used on a Secure-Boot-enabled machine. This process requires the use of sensitive keys and a passphrase that must only ever be known to and used by VotingWorks. Since the Trusted Build process is performed by a third-party vendor (SLI), a process to securely sign the image without compromising the keys or passphrase is needed. This page describes that process.

## Transferring an Unsigned Image from SLI to VotingWorks

Once SLI has created a Trusted Build image, the image and its virtual machine (VM) definition (an XML file) must be securely provided to VotingWorks. To transfer the image and definition, SLI uploads them to a shared S3 bucket accessible only to SLI and VotingWorks. This access is controlled via identity and access management (IAM) permission policies.

NOTE: This page uses a Trusted Build image named **vxadmin** as the example. Replace that with the appropriate image name, as necessary.

Once SLI has configured its S3 access and created a Trusted Build image, SLI uploads the image and its configuration file. Hashes of each file are generated so that SLI and VotingWorks can confirm files were not modified during the upload or download phases.

On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-unsigned-upload.sh vxadmin <version>
```

Once the SLI upload has completed, VotingWorks downloads and verifies the hash values of all files. On the VotingWorks secure build machine, while SLI observes:

```
sudo /home/admin/code/vxsuite-build-system/scripts/sb-unsigned-download.sh vxadmin <version>
```

Once the VotingWorks download has completed and been verified, and the VM has been successfully defined, VotingWorks can proceed with its Secure Boot signing process, while SLI observes.

## Secure Boot Signing

VotingWorks boots the VM, changes the vendor password, attaches a virtual device containing its Secure Boot signing keys, and selects the option to "Lock the System Down" from the vendor menu. When prompted, VotingWorks enters the passphrase for the Secure Boot signing keys.

When the process completes, the lock-down script displays the system hash in SHA256 and Signed Hash Validation (SHV) versions. These hashes are provided to SLI and the U.S. Election Assistance Commission (EAC) for official verification of the image.

## Transferring a Signed Image from VotingWorks to SLI

After the image is signed, VotingWorks uploads the signed image for SLI to download. While SLI observes, VotingWorks runs the following command on the VotingWorks secure build machine:

```
sudo /home/admin/code/vxsuite-build-system/scripts/sb-signed-upload.sh vxadmin <version>
```

Once this step has completed, SLI can download the files at any time. On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-signed-download.sh vxadmin <version>
```

Once SLI has completed the download, and hashes have been validated, the compressed image and signature can be provided to EAC for official use. At any point after submission to EAC, election officials and VotingWorks can verify the image hash as described under [verifying-the-image-installed-on-a-machine.md](../../imaging-machines/verifying-the-image-installed-on-a-machine.md "mention").
