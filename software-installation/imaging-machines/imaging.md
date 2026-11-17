# Imaging

First, prepare USB drives for imaging, following the instructions under [preparing-usb-drives-for-imaging.md](preparing-usb-drives-for-imaging.md "mention"). Then follow these steps:

1. Power off the machine.
2. Insert the vx-iso USB drive into the system. If this is a VxMarkScan or a VxScan, connect a keyboard as well. If there are not enough ports available, use a USB hub as provided by VotingWorks.
3. Power on the machine to begin booting vx-iso.&#x20;
   1. VotingWorks systems boot from the USB drive by default. If a system does not, select the USB drive from a BIOS or Boot Menu. For central system components, access the Boot Menu by pressing F9 during the boot sequence. For other components, contact VotingWorks for assistance.
4. Select "Install Image". vx-iso can be navigated with the keyboard. This option is auto-selected after 30 seconds.
5. If the machine already has Secure Boot keys installed, vx-iso does not prompt to install keys. If it does, contact VotingWorks for assistance. Install the keys only if they are known to be needed.
6. The application image(s) on the vx-iso USB drive are displayed. Select the number that identifies the correct image. If there is only one image, it is selected automatically.
7. The imaging process begins automatically after 10 seconds.&#x20;
8. When imaging completes, remove the USB drive as prompted. The system then reboots automatically.
9. After rebooting, the system automatically encrypts the `var` filesystem. If Secure Boot was not enabled when the image was installed, a note about needing to enable Secure Boot appears, and the machine boots into the BIOS. Once Secure Boot has been enabled and the system reboots, the encryption process completes.&#x20;
10. The /var partition encrypts and expands, followed by a reboot. If this is the first time that a VotingWorks application has been installed to a machine, the machine boots into the [Basic Configuration Wizard](basic-configuration-wizard.md). Proceed to that section. If the machine has been previously configured with a certified VotingWorks application of the same type, the [Basic Configuration Wizard](basic-configuration-wizard.md) is skipped.

Note: VotingWorks system software is installed to the directory path: `/vx/code/vxsuite`

The underlying storage for `/vx/code/vxsuite` depends on the hardware type. NVMe storage is used when available; otherwise, an eMMC storage device is used.
