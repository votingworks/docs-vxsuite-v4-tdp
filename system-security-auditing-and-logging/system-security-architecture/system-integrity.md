# System Integrity

The foundation of our system integrity solution is the TPM (described in greater detail under [cryptography.md](cryptography.md "mention")).

Our design for system integrity maps closely to that of ChromeOS:

1. The hard drive is partitioned such that executable code lives on the read-only partition `/`, and only `/var` and `/home` are mounted read/write for configuration, logs, and working data like scanned ballot images.
2. The read-only partition is verified by [dm-verity](https://source.android.com/docs/security/features/verifiedboot/dm-verity), which generates a hash tree of all the raw partition blocks, culminating in a single hash root for the entire read-only filesystem.
3. The kernel boot command line includes the dm-verity hash root as an argument, ensuring that Linux halts if the read-only partitions are not successfully verified against this hash root.
4. The BIOS is configured to only boot a properly signed bootloader+kernel+command-line, with public keys managed by VotingWorks and configured in the BIOS as secure boot keys. The bootloader+kernel+command-line that we want is set up as the default boot option in UEFI.
5. The private key described previously in [Access Control](access-control.md) is generated in the TPM and bound to Platform Configuration Registers (PCRs) that include the BIOS, the Secure Boot public keys, and the bootloader+kernel+command-line. Thus, this private key is only usable if the machine boots appropriately sanctioned source code with a hard drive whose read-only partitions are unmodified.

As a diagram:

<figure><img src="../../.gitbook/assets/Screenshot 2023-06-30 at 9.55.02 AM (1).png" alt=""><figcaption></figcaption></figure>

The integrity of the overall system is ensured because:

* Any change in the executable portion of the hard drive will be detected when dm-verity checks the hard drive blocks against its stored hashes.
* Any change in the hashes stored on disk will be detected against the mismatched root hash, present in the kernel boot command line.
* Any live changes to the read-only portion of the drive, even while the machine is already booted up, will be detected the moment Linux tries to read those modified blocks, as all disk reads are live-checked against the hashes.
* Any change in the kernel boot command line will be detected in two ways:
  * First, the TPM won’t unseal secrets since a change in the command line changes one of the PCR values, which means that the TPM’s policy check will fail.
  * Second, the system won’t even boot at all because the changed command line invalidates the signature on the bootloader+kernel+command-line, and UEFI will refuse to execute the now-improperly signed bootloader+kernel+command-line.

Thus, if the system boots, it means that the hard drive corresponds, by hashing, to the expected value that we baked into the bootloader+kernel+command-line and signed. If the system does not boot due to a failed cryptographic boot validation, it may be indicative of malware, so the user should make note of the error message and contact VotingWorks.

The only time that the system hash is expected to change is after a software update, which involves completely reimaging the machine per the process laid out in [imaging-machines](../../software-installation/imaging-machines/ "mention").

## Hard Drive Partitioning

Our system is configured so that `/var`, `/tmp`, and `/home` are mounted read-write, and `/` for everything else is mounted read-only. This requires writing logs and other runtime-generated VotingWorks data, e.g., scanned ballot images, to `/var`. Variable system configuration, e.g. timezone information, also needs to be redirected to `/var`. A USB mount point is pre-created at `/media/vx/usb-drive`.

## Protecting Critical Read-Write Data

In addition to locking down the `/` partition, the `/var` partition is encrypted and authenticated using `dm-crypt`. This ensures that, even if an attacker removes the physical hard drive and connects it to a different CPU, they cannot read or modify the contents of the `/var` partition in an attempt to make the VxSuite component behave differently.

Furthermore, as an extra layer of defense, every individual VxSuite component instance uses a unique random encryption key for its `/var` partition. Thus, if an attacker were to break the encryption on one VxSuite machine, they would have gained no advantage in penetrating a second machine. This is ensured through rekeying of the `/var` partition encryption on first boot of a VxSuite component.

## Signed Bootloader and Kernel

With Secure Boot, UEFI passes control to the bootloader only if the bootloader is appropriately signed. Then, the bootloader passes control to the kernel. We choose to bundle the bootloader, kernel, and command line that is used to run the kernel all as one, and to present that to the UEFI as the single executable whose signature should be verified before running. The three are combined into a single object file, along with the dm-verity root hash. This single object file is signed by VotingWorks secure boot private keys.

## Secure Boot

Every VotingWorks machine’s BIOS is configured with VotingWorks secure boot public keys, and the BIOS is configured to require Secure Boot. Thus, only a properly signed object file can serve as bootloader.

## Mounting USB Drives

When mounting USB drives, VxSuite always mounts them using standard Linux mount configuration options that makes files on the USB drive **NOT executable**. This further protects from any unauthorized software running, even in a transient fashion.



