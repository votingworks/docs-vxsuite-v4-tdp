# Preparing USB Drives for Imaging

Installing an image on a VotingWorks component, i.e., imaging a machine, requires a vx-iso USB drive with one or more VotingWorks application images stored in the "Data" partition. There is also a "Keys" partition that can optionally contain VotingWorks Secure Boot public keys, necessary if a machine has not had these keys installed yet.

USB drives used as vx-iso drives must be zeroed out before first use. Zeroing also ensures that the USB drive is empty and no longer contains any previous data before use as installation media. To zero out a drive, run the following command, substituting `/dev/sdX` with the appropriate path to the USB drive, e.g., `/dev/sda`:

```
sudo dd if=/dev/zero of=/dev/sdX bs=8M && sudo sync
```

Drives provided by VotingWorks are already initialized with this process and contain the appropriate vx-iso release for installing an application image. Only the appropriate application image(s) need to be copied to them. To create a new vx-iso USB drive, contact VotingWorks for assistance.

### Copying an image file to a vx-iso USB drive

This example assumes a signed vxadmin image on the build machine, located in the root user's home directory and named **vxadmin-signed.img.lz4**. The root user's home directory is the default location of the signed image file, so the path of the example image is:

```
~root/vxadmin-signed.img.lz4
```

The example also assumes that the USB drive is automatically mounted by the **vx** user, with the **Data** partition located at:

```
/media/vx/Data
```

1. As the **vx** user, verify that the USB drive is mounted at the path above:

```
ls /media/vx/Data/
```

The command returns without an error. It lists any images already on the USB drive; deleting them is optional.

2. To copy the image to the USB drive, run the following command as the **vx** user:

```
sudo cp ~root/vxadmin-signed.img.lz4 /media/vx/Data/ && sudo sync
```

3. When the copy and sync complete, eject and remove the USB drive. It is now ready to image a machine.

Repeat this process with any other vx-iso USB drives and VotingWorks image files as required.
