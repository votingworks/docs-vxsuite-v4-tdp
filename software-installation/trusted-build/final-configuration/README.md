# Final Configuration

While you can perform this final phase in the offline VM created in the previous step, we recommend cloning the offline VM for each specific VotingWorks application to save time. By cloning the offline VM, you only need to perform the application specific configuration since they share the same base application code.

In the following steps, the **vxadmin** VM will be referenced. In future tests or builds, these steps can be repeated for each different VotingWorks application: **vxcentralscan**, **vxscan**, and **vxmark**.

1. To clone the offline VM, run the following command on the build machine:

Copy

```
sudo virt-clone -o offline -n vxadmin --auto-clone
```

This command creates a byte-for-byte clone of the offline VM, along with all settings, including network functionality disabled at the VM level.

1. Open virt-manager (if not already open):

Copy

```
sudo virt-manager
```

1. Double-click the vxadmin VM
2. Press the Start button ▶️
3. Once the VM has initialized, log in with username: **vx** and password: **votingworks**
4. To ensure the console displays correctly, select the “View” menu option, then “Resize to VM”
5. In the vxadmin VM terminal:

Copy

```
cd ~/code/vxsuite-complete-system
./setup-machine.sh
```

1. You will be guided through several questions.

```
Select the machine type from the available options
set vx-admin passsword
type it again to confirm
Answer no for sudo privileges
Enter sudo password for vx (votingworks)
```

1. After the script finishes, the VM will reboot. You will see a white screen displaying “Card Reader Not Detected”. In the VM menu, select Virtual Machine → Shut Down → Shut Down. Close the VM window once shutdown is complete.
2. You will now need to perform the [Secure Boot Signing](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/final-configuration/secure-boot-signing) process with VotingWorks. Once that process is completed, the VM is signed for use with Secure Boot.

At this point, you are ready to install the image. You can find those instructions in [Installing an Image via vx-iso](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/installing-an-image-via-vx-iso/installing-a-votingworks-image).
