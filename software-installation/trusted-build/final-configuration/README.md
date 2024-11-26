# Final Configuration

We'll now clone the offline VM to prepare images for specific machine types, i.e., VxAdmin, VxCentralScan, VxMark, and VxScan. We'll create one clone/VM per machine type.

In the following steps, the **vxadmin** VM will be referenced, but these steps can be repeated for each machine type: **vxcentralscan**, **vxmark**, and **vxscan**.

1. To clone the offline VM, run the following command on the build machine:

```
sudo virt-clone -o offline -n vxadmin --auto-clone
```

* This command creates a byte-for-byte clone of the offline VM, along with all settings, including network functionality disabled at the VM level.

2. Open virt-manager if not already open:

```
sudo virt-manager
```

3. Double-click the **vxadmin** VM.
4. Press the start button ▶️.
5. Once the VM has initialized, log in with username **vx** and password **votingworks**.
6. To ensure that the console displays correctly, select "View" > "Resize to VM".
7. In the VM terminal window, run the following commands:

```
cd ~/code/vxsuite-complete-system
./setup-machine.sh
```

8. You will be guided through several prompts.
9. Select the number of the machine type that you intend to build.

```
Welcome to VxSuite. THIS IS A DESTRUCTIVE SCRIPT. Ctrl-C right now if you don't know for sure what you're doing.
Which machine are we building today?

1. VxAdmin
2. VxCentralScan
3. VxMark
4. VxScan
```

10. Type "N" when asked whether this image is for QA.

```
Is this image for QA, where you want sudo privileges, terminal access via TTY2, and the ability to record screengrabs? [y/N]
```

11. Type "y" when asked whether this is an official release image.

```
Is this additionally an official release image? [y/N]
```

12. Set a password for the `vx-vendor` user. This password will not meaningfully be used as the vendor menu on a production image is only accessible via a vendor card.
13. After the script finishes, the VM will reboot. You will see a white screen displaying “Card Reader Not Detected”. In the VM menu, select "Virtual Machine" > "Shut Down" > "Shut Down". Close the VM window once shutdown is complete.
14. You will now need to perform the [Secure Boot Signing](https://docs.voting.works/vxsuite-tdp-v3.1/trusted-build/final-configuration/secure-boot-signing) process with VotingWorks. Once that process is completed, the VM and corresponding image will be ready for use with Secure Boot.

At this point, you are ready to install the image. You can find those instructions in [Imagine Machines](../../imaging-machines/).
