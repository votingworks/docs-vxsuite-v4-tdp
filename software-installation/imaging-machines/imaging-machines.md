# Imaging Machines

First make sure that you've prepared USB drives for imaging, following the instructions under [preparing-usb-drives-for-imaging.md](preparing-usb-drives-for-imaging.md "mention"). Then follow these steps:

1. Power off the machine.
2. Insert both the vx-iso and image USB drives into the system. If this is a VxMark or a VxScan, connect a keyboard as well. If there aren't enough ports available, use a USB hub as provided by VotingWorks.
3. Power on the machine. Our machines our configured to auto-boot from a bootable USB drive when connected and should auto-boot to vx-iso. You can navigate vx-iso with the keyboard.
4. Select "Write an image". This option will be auto-selected in 10 seconds.
5. If the machine already has Secure Boot keys installed, it should not prompt you to install keys. If it does for some reason, but you know Secure Boot keys to be installed, opt not to install Secure Boot keys. Only if you know the keys need to be installed should you opt to install them.
6. The images on the image USB drive will be displayed. Select the index of the correct image.
7. Enter 27 for the final expected size of the image in GB.
8. Confirm your selections and wait for imaging to complete.
9. Once imaging completes, remove the USB drives and press "Enter" to reboot.
10. On reboot, you should see a prompt for a passphrase. This passphrase is used to decrypt the machine's /var partition so that it can be re-encrypted via the TPM. Enter "insecure" — this passphrase is not relevant to our security architecture. If Secure Boot is not enabled, you'll instead see a note about needing to enable Secure Boot. The machine will auto-boot you into the BIOS. On reboot after that, you should see the passphrase prompt.
11. The /var partition should encrypt and expand, and you should then find yourself in Basic Configuration Wizard. Proceed to that section.

### VxMark Boot Order Fix

**On VxMark**, if you find yourself on an unexpected screen after the above steps, e.g., a Secure Boot error screen or booting straight into a previously installed image, you may need to manually edit the VxMark boot order. You can follow these instructions to do so:

1. Power off the machine.
2. Insert the vx-iso USB drive.
3. Power on the machine and auto-boot to vx-iso.
4. Use "Ctrl+C" to leave the main vx-iso interface and access a terminal.
5. Type `efibootmgr` to list out the boot entries. The output will look something like this:

```
BootCurrent: 0001
Timeout: 0 seconds
BootOrder: 0000,0001,0002
Boot0000* USB HDD
Boot0001* vxadmin - Installed 20241030 
Boot0002* vxadmin-signed - Installed 20241031
```

6. Identify the boot entry for the recently installed image. Let's say in this case we want vxadmin-signed, Boot0002.
7. Run the following command, replacing the index, to make that entry the first in the boot order after the USB drive:

```
efibootmgr -o 0002
```
