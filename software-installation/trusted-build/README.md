# Trusted Build

The VotingWorks build process consists of three distinct build phases: [online](online-phase.md), [offline](offline-phase.md), and [final configuration](final-configuration/). The build process uses an inventory definition containing all the necessary information for a Trusted Build. All three phases are executed within a separate virtual machine (VM) managed by the [virt-manager](https://virt-manager.org/) tool, running on a Debian 12 operating system.

In the online phase, the build process utilizes a base Debian 12 VM with network access enabled. All necessary code repositories and build tools are securely retrieved for use during the offline phase.

In the offline phase, the build process utilizes a clone of the online VM with network access disabled.&#x20;

In the final configuration phase, the build process utilizes clones of the offline VM to prepare images for specific machine types, i.e., VxAdmin, VxCentralScan, VxMark, and VxScan.

After completing the final configuration phase, an unlocked installation image has been created. While this image is not appropriate for production use, it can be used for testing.

For a final production image, an additional step is required to securely sign the installation image for use with Secure Boot enabled systems, described under [Secure Boot Signing](final-configuration/secure-boot-signing.md).
