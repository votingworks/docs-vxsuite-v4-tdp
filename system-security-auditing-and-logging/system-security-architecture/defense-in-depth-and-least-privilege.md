# Defense-in-Depth and Least Privilege

Beyond the application-level protections and system integrity assurances designed to prevent unauthorized access and the execution of unauthorized software, VxSuite is also designed with defense-in-depth and least-privilege principles. This limits the impact of a failure of some defenses due to unforeseen bugs or novel attacks.

## Minimal Operating System

VxSuite runs a modern, stripped down Linux installation with the minimum number of packages to reduce the attack surface of any unexpected partial penetration. The set of packages is manually curated by VotingWorks and specified in the VxSuite installation manifests when building a base Linux image.

### DEP and ASLR

The Linux OS makes use of data execution prevention (DEP) and address space layout randomization (ASLR). These exploit mitigation strategies provide a low-level layer of protection against a variety of vulnerabilities. VotingWorks has verified that these mechanisms are active via the following commands:

```
# For DEP, verify that the nx flag is set on CPUs
grep -m1 ' nx ' /proc/cpuinfo

# For ASLR, verify that the output of this is 1 or 2, not 0
cat /proc/sys/kernel/randomize_va_space
```

## No Root User Access

Once a VxSuite image is built, access for the root user is shut down and that shutdown is locked in via Secure Boot verification of the root partition.

## Narrow Superuser Functions

When a VxSuite function requires superuser access, that access is captured as a minimal shell script, and the appropriate VxSuite Linux user is granted sudo permissions on that shell script alone. For example, on a VxSuite production machine, no user has the ability to call the `mount` command. Instead, for mounting USB drives, VxSuite includes a shell program that is only capable of mounting and unmounting USB drives at the `/media/vx/usb-drive` mount point, and the `vx-services` user is granted superuser privileges when calling that script only. The full script for this example is available at [https://github.com/votingworks/vxsuite/blob/v4.1.1/libs/usb-drive/scripts/mount.sh](https://github.com/votingworks/vxsuite/blob/v4.1.1/libs/usb-drive/scripts/mount.sh).

## Minimal Window Manager

VxSuite runs a minimal window manager, Openbox, which is built to have very few capabilities. In addition, VotingWorks configures Openbox to turn off all keyboard shortcuts and contextual menus, so an attacker who plugs in a mouse or a keyboard has no window manager shortcuts or menus available.

## Compartmentalization of Permissions and Separation of Auth

All processes that a user can directly interact with in VxSuite run as user `vx-ui`. The processes that access the smart card reader or perform data processing services run as user `vx-services`.

The `vx-services` Linux user has a set of permissions allowing it to access the scanner, printer, and smart card reader. It is configured, like the root user, to not have a password, so no interactive user can log in as `vx-services` and utilize those privileges. The services that run under the `vx-services` user account offer their services over local HTTP, with well-formed semantics as to what actions they allow. The authentication status is checked on the backend, by `vx-services`, so actions can only be taken if a valid authentication session is open.

Meanwhile, if a user were to break out of the constraints placed on the window manager and obtain a shell, that shell would run as `vx-ui`, which has the ability to call into services run as `vx-services`, but does not itself have the direct privileges of `vx-services`. Thus, an attacker that penetrates the first line of defense would remain limited to the privileges of `vx-ui`.
