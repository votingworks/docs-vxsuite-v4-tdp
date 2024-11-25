# Offline Phase

1. Open virt-manager if not already open:

```
sudo virt-manager
```

2. Double-click the **offline** VM.
3. Press the start button ▶️.
4. Once the VM has initialized, log in with username **vx** and password **votingworks**.
5. To ensure that the console displays correctly, select "View" > "Resize to VM".
6. In the VM terminal window, validate that networking is automatically disabled in the offline VM using the following command:

```
ping -c2 google.com
```

* This command should either time out or immediately error with a failure in name resolution.

7. Ensure that the USB drive created in the online phase is attached to the build machine.
8. To make the USB available to the offline VM, select "Virtual Machine" > "Redirect USB Device". In the dialog box that opens, select the USB drive that you attached and close the dialog.
9. The USB drive will usually be available as `/dev/sda1`. To confirm, you can use:

```
lsblk /dev/disk/by-id/usb*part* --noheadings --output PATH
```

* If it’s accessible by a different path, that’s fine, just make a note of it and use that path in the following steps as appropriate.

10. Run the following commands:

```
sudo mkdir -p /mnt/vx/usb-drive
sudo mount /dev/sda1 /mnt/vx/usb-drive
sudo /mnt/vx/usb-drive/vxsuite-build-system/scripts/tb-import-from-usb.sh
cd ~/code/vxsuite-build-system
./scripts/tb-run-offline-phase.sh <inventory-name>
```

11. Once the offline phase completes, the base VotingWorks application has been built. You can now shut down the offline VM:

```
sudo shutdown -h now
```
