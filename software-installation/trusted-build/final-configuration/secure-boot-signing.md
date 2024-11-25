# Secure Boot Signing

To finalize an image for production use, it is necessary to implement Secure Boot. This process requires the use of sensitive keys and a passphrase that should only ever be known to and used by VotingWorks. Since the Trusted Build process is performed by a third-party vendor (SLI), a process to securely sign the image without compromising the keys or passphrase is needed. This document describes that process.

**Transferring An Image**

Once SLI has created a Trusted Build image, the image and its VM definition (an xml file) must be securely provided to VotingWorks. To transfer the image and definition, SLI will upload to a shared S3 bucket only accessible to SLI and VotingWorks. This access will be controlled via IAM permission policies.

NOTE: For documentation purposes, we will use a Trusted Build image named **vxadmin**. Replace that with the appropriate image name, as necessary.

Once SLI has configured their S3 access and created a Trusted Build image, they will need to upload the image and its configuration file. Additionally, hashes of each file will be generated so SLI and VotingWorks can confirm files were not modified during the upload or download phases.

1. On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-unsigned-upload.sh vxadmin
```

1. Once the SLI upload has completed, VotingWorks will download and verify the hash values of all files. On the VotingWorks secure build machine, while SLI observes:

```
sudo code/vxsuite-build-system/scripts/sb-unsigned-download.sh vxadmin
```

1. Once the VotingWorks download has completed and verified and the VM has been successfully defined, normal Secure Boot processes can be followed, while SLI observes.
2. Once the Secure Boot configuration has been completed, VotingWorks will retrieve the image signature from the admin menu. This hash will be provided to SLI/EAC for official verification of the image.
3. Now that the image has been securely signed, VotingWorks will upload the signed image for SLI to later download. While SLI observes, VotingWorks will run the following command on the secure build machine:

```
sudo code/vxsuite-build-system/scripts/sb-signed-upload.sh vxadmin
```

1. Once this step has completed, SLI can download the files at their convenience. On the SLI build machine:

```
sudo su -
/home/vx/code/vxsuite-build-system/scripts/sb-signed-download.sh vxadmin
```

1. Once SLI has completed the download and hashes are validated, the compressed image and signature can be provided to EAC for use by election officials. At any point after submission to EAC, election officials can verify the image hash via the vx-iso tool.
