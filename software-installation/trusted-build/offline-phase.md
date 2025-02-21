# Offline Phase

1. To create the **offline** VM with networking disabled, run the following command on the build machine:

```
cd ~/code/vxsuite-build-system
./scripts/tb-create-offline-vm.sh
```

2. Open virt-manager if not already open:

```
sudo virt-manager
```

3. Double click the **offline** VM.
4. Press the start button ▶️.
5. Once the VM has initialized, log in with username **vx** and password **votingworks**.
6. To ensure that the console displays correctly, select "View" > "Resize to VM".
7. In the VM terminal window, validate that networking is automatically disabled in the offline VM using the following command:

```
ping -c2 google.com
```

* This command should either time out or immediately error with a failure in name resolution.

8. To execute the offline phase, run the following commands:

```
cd ~/code/vxsuite-build-system
./scripts/tb-run-offline-phase.sh <inventory-name>
```

9. Once the offline phase completes, the base VotingWorks application has been built. You can now shut down the offline VM:

```
sudo shutdown -h now
```
