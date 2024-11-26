# Online Phase

1. Open virt-manager:

```
sudo virt-manager
```

2. Double-click the **online** VM.
3. Press the start button ▶️.
4. Once the VM has initialized, log in with username **vx** and password **votingworks**.
5. To ensure that the console displays correctly, select "View" > "Resize to VM".
6. In the VM terminal window, run the following commands:

```
mkdir ~/code && cd ~/code
git clone https://github.com/votingworks/vxsuite-build-system
cd ~/code/vxsuite-build-system
./scripts/tb-run-online-phase.sh <inventory-name> 
```

* You will be prompted for the sudo password.

7. The online phase will take awhile to complete.
8. Once it finishes, you need to attach a USB drive to the build machine. This USB drive will be used to transfer all necessary tools and code to the offline VM.
9. To make the USB drive available to the online VM, select "Virtual Machine" > "Redirect USB Device". In the dialog box that opens, select the USB drive that you attached and close the dialog.
10. In the online VM terminal:

```
cd ~/code/vxsuite-build-system
./scripts/tb-export-to-usb.sh <inventory-name>
```

11. You will be prompted to select the USB drive. Once selected, all necessary code repositories and build tools will be exported to the USB drive. After the export is complete, you can shut down the online VM:

```
sudo shutdown -h now
```
