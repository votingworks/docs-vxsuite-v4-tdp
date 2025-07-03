# Imaging

First make sure that you've prepared USB drives for imaging, following the instructions under [preparing-usb-drives-for-imaging.md](preparing-usb-drives-for-imaging.md "mention"). Then follow these steps:

1. Power off the machine.
2. Insert the vx-iso USB drive into the system. If this is a VxMark or a VxScan, connect a keyboard as well. If there aren't enough ports available, use a USB hub as provided by VotingWorks.
3. Power on the machine to begin booting vx-iso.&#x20;
   1. By default, VotingWorks systems should boot from the USB. If not, you will need to select the USB drive from a BIOS or Boot Menu. For central system components, you can access the Boot Menu by pressing F9 during the boot sequence. For other components, please reach out to VotingWorks for assistance.
4. Select "Install Image". You can navigate vx-iso with the keyboard. This option will be auto-selected after 30 seconds.
5. If the machine already has Secure Boot keys installed, it should not prompt you to install keys. If it does for some reason, you should reach out to VotingWorks for assistance. Only if you know the keys need to be installed should you opt to install them.
6. The application image(s) on the vx-iso USB drive will be displayed. Select the number that identifies the correct image. In the event there is only one image, it will be automatically selected.
7. The imaging process will begin automatically after 10 seconds.&#x20;
8. Once imaging completes, remove the USB drive as prompted. The system will reboot automatically after 10 seconds.
9. After rebooting, the system will perform an automatic encryption of the `var` filesystem. If Secure Boot was not enabled when the image was installed, you'll see a note about needing to enable Secure Boot. The machine will auto-boot you into the BIOS. Once Secure Boot has been enabled and the system reboots, the encryption process should complete successfully.&#x20;
10. The /var partition should encrypt and expand, followed by a reboot. If this is the first time that a VotingWorks application has been installed to a machine, you should find yourself in the [Basic Configuration Wizard](basic-configuration-wizard.md). Proceed to that section. If the machine has been previously configured with a certified VotingWorks application of the same type, the [Basic Configuration Wizard](basic-configuration-wizard.md) will be skipped.

Note: VotingWorks system software will be installed to the directory path: `/vx/code/vxsuite`

The underlying storage for `/vx/code/vxsuite` will depend on the hardware type. By default, NVMe storage is used. In the event an NVMe storage device is not available, an eMMC storage device will be used.
