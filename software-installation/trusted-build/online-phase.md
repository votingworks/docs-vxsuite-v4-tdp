# Online Phase

1. Open virtmanager:

```
sudo virt-manager
```

1. Double-click the **online** VM
2. Press the Start button ▶️
3. Once the VM has initialized, log in with username: **vx** and password: **votingworks**
4. To ensure the console displays correctly, select the “View” menu option, then “Resize to VM”
5. In the terminal window, run the following commands:

```
mkdir ~/code && cd ~/code
git clone 
https://github.com/votingworks/vxsuite-build-system
cd ~/code/vxsuite-build-system
./scripts/tb-run-online-phase.sh <inventory name> 
```

* You will be prompted for sudo password.

1. The online phase will take awhile to complete. Once it finishes, you need to attach a USB drive to the build machine. This USB drive will be used to transfer all necessary tools and code to the offline VM. To make the USB available to the online VM:
2. From the menu, select Virtual Machine. In the dropdown, select Redirect USB Device. In the dialog box that opens, select the USB drive you attached, then close the dialog.
3. In the online VM terminal:

```
cd ~/code/vxsuite-build-system
./scripts/tb-export-to-usb.sh <inventory name>
```

1. You will be prompted to select the USB drive. Once selected, all necessary code repositories and build tools will be exported to the USB. After the export is complete, you can shut down the online VM:

```
sudo shutdown -h now
```
