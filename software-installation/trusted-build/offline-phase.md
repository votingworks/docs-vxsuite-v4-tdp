# Offline Phase

Open virt-manager (if not already open):

```
sudo virt-manager
```

1. Double-click the **offline** VM
2. Press the Start button ▶️
3. Once the VM has initialized, log in with username: **vx** and password: **votingworks**
4. To ensure the console displays correctly, select the “View” menu option, then “Resize to VM”
5. In a terminal window, validate that [networking is automatically disabled](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/virt-manager-network-access-and-troubleshooting) in the offline VM through the following command:

```
ping -c2 google.com
```

This command should either time out or immediately error with a failure in name resolution.

1. Ensure the USB drive created in the online phase is attached to the build machine.
2. Make the USB available to the offline VM:
   1. From the menu, select Virtual Machine
   2. In the dropdown, select Redirect USB Device
   3. In the dialog box that opens, select the USB drive you attached, then close the dialog
   4. The USB drive will usually be available as /dev/sda1. To confirm, you can use:

```
lsblk /dev/disk/by-id/usb*part* --noheadings --output PATH
```

If it’s accessible by a different path, that’s fine, just make a note of it and use that path in the following steps as appropriate.

```
sudo mkdir -p /mnt/vx/usb-drive
sudo mount /dev/sda1 /mnt/vx/usb-drive
sudo /mnt/vx/usb-drive/vxsuite-build-system/scripts/tb-import-from-usb.sh
cd ~/code/vxsuite-build-system && ./scripts/tb-run-offline-phase.sh <inventory name>
```

Once the offline phase completes, the base VotingWorks application has been built. You can now shut down the offline VM via:

1. Once the offline phase completes, the base VotingWorks application has been built. You can now shut down the offline VM via:

```
sudo shutdown -h now
```
