# Installing Debian 12 on VxBuild

## Create Debian 12 USB Install Drive <a href="#create-debian-12-usb" id="create-debian-12-usb"></a>

To install Debian 12 on the build machine (VxBuild), you will need to download the latest Debian 12 amd64 installer file here: [Latest Debian Release](https://www.debian.org/releases/stable/debian-installer/).

You should use a blank USB drive for the install drive. The process described below will wipe any existing content.

To create a USB install drive with the downloaded .iso file:

1. Ensure that the USB drive is available to the system. By default, it tries to attach as the `/dev/sda` device. An easy way to verify this is via the following command:

```
lsblk /dev/disk/by-id/usb*part* --noheadings --output PATH
```

2. If the USB drive is not attached as the `/dev/sda` device, that’s ok. Simply replace `/dev/sda` with the device that your USB drive did attach to.

* NOTE: The command below should not include any number as part of the device path. For example, if the above command returns `/dev/sda1`, you must use `/dev/sda` as the path in the next command.

3. Now that you know the correct device path, you can create the USB install drive via the following command:

```
dd if=/path/to/debian-12.8.0-amd64-netinst.iso of=/dev/sda bs=4M && sync
```

* NOTE: At the time of this writing, the latest stable release is 12.8. Please update to the appropriate filename if you use a newer version.

4. Once the above command completes, you can safely remove the USB install drive from your system.

## Installing to VxBuild <a href="#installing-to-vxbuild" id="installing-to-vxbuild"></a>

1. Before turning the VxBuild system on, insert the USB install drive created in the previous step.
2. Boot the system from the USB install drive. (After powering the build machine on, begin pressing F12 until it enters the Boot Menu)
3. You will be presented with the following screen:

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252F09WHiEOF7H3usr80ZGiD%252F0.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=f73c5d27\&sv=1)

1. Select Graphical Install and press Enter

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252F8j9qEENAJthFV6fo5rOQ%252F1.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=bc02f88a\&sv=1)

1. Select your preferred language and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FMNHob9ZRDf1YCiTmd0gz%252F2.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=e043e4eb\&sv=1)

1. Select your location and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FkrFJ7GRBx5ZltffXuR1m%252F3.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=7775127c\&sv=1)

1. Select your keyboard layout and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FUUtKLL9DvVsUh7LDEyyp%252F4.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=7a340f2a\&sv=1)

1. Select your network device (may differ from screenshot) and click Continue.
2. If using a wireless connection, follow the next steps. If using a wired connection, it will configure automatically.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FFBRHtURKem0a5eetyPlC%252F5.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=6b2396f7\&sv=1)

1. Select your network device (may differ from screenshot) and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252F0hDzW4VHBx9s9FocEhlf%252F6.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=338b6cf9\&sv=1)

1. Select WPA/WPA2 PSK and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FgAHj4dCXdG6AljVgsIPa%252F7.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=3309aad0\&sv=1)

1. Enter your wireless network password and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FLdJEwIoCiLdZ0BGl1h3j%252F8.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=e0cf07b1\&sv=1)

1. Enter “VxBuild” for the hostname and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252Fjt4H0gWQRDFBV6x93s7s%252F9.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=c5a6faa5\&sv=1)

1. Leave the domain name blank and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FR0TOGQvv0VHMCSjRG8rL%252F10.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=ce40fa40\&sv=1)

1. Set the root user password and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FdmS6R3cltQgtSm6RaD02%252F11.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=fbe31cd9\&sv=1)

1. Enter “Vx” for the full name for the new user and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252F82k6hen6zKV7f2eQQncB%252F12.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=33df2793\&sv=1)

1. Enter “vx” as the username and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FikvpQvLo4MF8ssiwIj8k%252F13.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=232420bf\&sv=1)

1. Enter a password for the “vx” user and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FKVnkr8yuS6JaPBeFtA3K%252F14.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=5cdc782b\&sv=1)

1. Select your timezone and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FcqphTO8y5pyX6ljP5Op6%252F15.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=86ee9728\&sv=1)

1. Select “Guided - use entire disk” and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FBOYwkN2QVvaMt5sbL9qs%252F16.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=9c662ea7\&sv=1)

1. Select the “/dev/nvme0n1” disk and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FCp4Wt5Ql8a35p1IJsCRJ%252F17.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=f37acaeb\&sv=1)

1. Select “All files in one partition” and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FqOlliXREG8nY9MjA9Gx7%252F18.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=6eb40205\&sv=1)

1. Select “Finish partitioning and write changes to disk” and click Continue.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FdW3ElI4p5qDV9wUmhPk8%252F19.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=affa5c63\&sv=1)

1. Select “Yes” and click Continue.
2. The base OS installation will now begin. During the installation you will be asked to answer questions related to package management.

![](https://docs.voting.works/~gitbook/image?url=https%3A%2F%2F1186688720-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FqrzXyISkrU67zmViGRWG%252Fuploads%252FvAhPJRMeklLPp644P85y%252F20.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=8d3cd0a8\&sv=1)

1. Select “United States” and click Continue.
2. Select “deb.debian.org” and click Continue.
3. Leave the proxy information blank and click Continue.
4. The installation process will continue automatically. You will be asked to configure “popularity-contest”.
5. Select “No” and click Continue.
6. Select the options as shown above and click Continue.
7. The installation process will continue. Once it completes, you will be presented with a final screen confirming it was successful.
8. Remove the USB drive and Click Continue.
9. The system will reboot and automatically start Debian 12
10. Log in with the “vx” user and password you created during the installation process.
11. Several basic configuration prompts will be displayed.
12. Select Next.
13. Select your keyboard preference and click Next.
14. Turn off Location Services and click Next.
15. Do not configure any Online Accounts. Select Skip.
16. Click the “Start Using Debian GNU/Linux” button. The dialog will be closed.

**Grant sudo privileges**

The “vx” user needs to be granted sudo privileges related to configuring and initializing the build environment tools. To do this, open a terminal window. (TODO: terminal instructions)

1. The “vx” user needs to be granted sudo privileges related to configuring and initializing the build environment tools. To do this, open a terminal window. (TODO: terminal instructions)
2. As the “vx” user, you will temporarily log in to the “root” account.

```
su -
<enter root user password>
```

1. You will see your terminal window prompt change to “root@VxBuild”. To grant the “vx” user sudo privileges, run the following command as root.

```
echo "vx ALL=NOPASSWD: ALL" > /etc/sudoers.d/vx
exit
```

1. You will see your terminal window prompt change to “vx@VxBuild”. You are now the “vx” user instead of the “root” user. To confirm sudo privileges, run the following command:

```
sudo whoami
```

1. The command should return “root”. This confirms sudo privileges have been granted correctly.
