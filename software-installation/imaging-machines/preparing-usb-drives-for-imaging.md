# Preparing USB Drives for Imaging

To install an image on a VotingWorks component, i.e., to image a machine, you need two USB drives:

* A vx-iso USB drive — [vx-iso](https://github.com/votingworks/vx-iso) is our VotingWorks-specific ISO installer program.
* An image USB drive — This is an empty USB drive with two partitions, a "Data" partition that can contain as many VotingWorks images as space allows and a "Keys" partition that can optionally contain the VotingWorks Secure Boot public keys, necessary if a machine hasn't had these keys installed yet.

Note: If you have existing drives that are properly partitioned, you can skip these steps and simply copy a VotingWorks image file directly to the USB. Those instructions can be found at the bottom of this page in the [#copying-an-image-file-to-a-previously-configured-usb-drive](preparing-usb-drives-for-imaging.md#copying-an-image-file-to-a-previously-configured-usb-drive "mention") section.

Clone the vx-iso repo for the tooling necessary to prepare the above:

```
git clone https://github.com/votingworks/vx-iso.git
cd vx-iso
```

[Follow these instructions](https://github.com/votingworks/docs-vxsuite-v4/blob/main/software-docs/README-vx-iso.md) to create a vx-iso and/or image USB drive.

{% hint style="info" %}
If this is SLI, we have provided you with vx-iso USB drives so that you don't need to prepare them from scratch.
{% endhint %}

You'll need access to the relevant images and optionally the VotingWorks Secure Boot **public** keys. Both of these are stored on a private S3 bucket, though they're not sensitive, and VotingWorks can prepare temporary links to grant access to them.

{% hint style="info" %}
If this is SLI, you do not need to create data drives with the VotingWorks Secure Boot public keys. Secure Boot has already been configured on all your machines.
{% endhint %}

### Copying an image file to a previously configured USB drive

For this example, we will assume that you have a signed vxadmin image on the build machine. It will be located in the root user's home directory and be named **vxadmin-signed.img.lz4**

We will also assume the USB drive is automatically mounted by the **vx** user, with the **Data** partition located at:&#x20;

```
/media/vx/Data
```

As the **vx** user, first verify the USB is mounted at the path above. An easy way to test is with the following command:

```
ls /media/vx/Data/
```

That command should return without an error. It may list one or more images if they were already on the USB drive. That's ok. (You can delete any existing images from the USB drive if you like, but it is not necessary.)

Since the signed image file is located in the root user's home directory by default, we'll use that path. As mentioned earlier, we will use a vxadmin image for this example. That path would be:

```
~root/vxadmin-signed.img.lz4
```

To copy the image to the USB drive, run the following command as the **vx** user:

```
sudo cp ~root/vxadmin-signed.img.lz4 && sudo sync
```

Once the copy and sync completes, you can eject the USB drive and remove it. It is now ready to image a machine. Repeat this process with any other USB drives and VotingWorks image files as required.&#x20;



