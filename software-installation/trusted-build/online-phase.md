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

7. The online phase will take awhile to complete. Once it finishes, you can shut down the online VM:

```
sudo shutdown -h now
```
