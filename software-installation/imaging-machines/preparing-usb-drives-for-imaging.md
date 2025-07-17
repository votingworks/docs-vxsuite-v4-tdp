# Preparing USB Drives for Imaging

To install an image on a VotingWorks component, i.e., to image a machine, you need a vx-iso USB drive with one or more VotingWorks application images stored in the "Data" partition. There is also a "Keys" partition that can optionally contain VotingWorks Secure Boot public keys, necessary if a machine hasn't had these keys installed yet.

USB drives used as vx-iso drives must be zeroed out before first use. This step will also ensure the USB drive is empty and no longer contains any previous data prior to use as installation media. You can zero out a drive with the following command, substituting `/dev/sdX` with the appropriate path to the USB you are using, e.g. `/dev/sda`&#x20;

```
sudo dd if=/dev/zero of=/dev/sdX bs=8M && sudo sync
```

Drives provided by VotingWorks are already initialized with this process and contain the appropriate vx-iso release for installing an application image. You will only need to ensure the appropriate application image(s) are copied to the vx-iso USB drive. If you are creating your own vx-iso USB drive, please contact VotingWorks for assistance.

### Copying an image file to a vx-iso USB drive

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
sudo cp ~root/vxadmin-signed.img.lz4 /media/vx/Data/ && sudo sync
```

Once the copy and sync completes, you can eject the USB drive and remove it. It is now ready to image a machine. Repeat this process with any other vx-iso USB drives and VotingWorks image files as required.&#x20;



