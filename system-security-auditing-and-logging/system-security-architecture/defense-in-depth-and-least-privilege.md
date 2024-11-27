# Defense-in-Depth and Least Privilege

Beyond the application-level protections and system integrity assurances built to ensure that unauthorized access is thwarted and unauthorized software cannot be executed, VxSuite is also designed with defense-in-depth and least-privilege principles. This ensures that a failure of some defenses, due to unforeseen bugs or novel attacks, can be limited in its impact.

## Minimal Operating System

VxSuite runs a modern, stripped down Linux installation with the minimum number of packages to reduce the attack surface of any unexpected partial penetration. The set of packages is manually curated by our team and specified in our installation manifests when building a base Linux image.

## No Root User Access

Once a VxSuite image is built, access for the root user is shut down and that shutdown is locked in via secure-boot verification of the root partition.&#x20;

## Narrow Superuser Functions

When a VxSuite function requires superuser access, that access is captured as a minimal shell script, and the appropriate VxSuite Linux user is granted sudo permissions on that shell script alone. For example, on a VxSuite production machine, no user has the ability to call the `mount` command. Instead, when mounting USB drives, we have crafted a shell program that is only capable of mounting and unmounting USB drives at the `/media/usb-drive` mount point, and the `vx-services` user is granted superuser privileges when calling that script only. The full script for this example is available at [https://github.com/votingworks/vxsuite/blob/main/libs/usb-drive/scripts/mount.sh](https://github.com/votingworks/vxsuite/blob/main/libs/usb-drive/scripts/mount.sh)

## Minimal Window Manager

VxSuite runs a minimal window manager, Openbox, which is built to have very few capabilities. In addition, we configure Openbox so as to turn off all keyboard shortcuts and contextual menus. Even if an attacker were able to plug in a mouse or a keyboard, they would be unable to get very far.

## Compartmentalization of Permissions and Separation of Auth

All processes that a user can directly interact with in VxSuite run as user `vx-ui`. The processes that access the smart card reader or perform data processing services run as user `vx-services`.&#x20;

The `vx-services` Linux user has a set of permissions allowing it to access the scanner, printer, and smart card reader. It is configured, like the root user, to not have a password, so no interactive user can log in as `vx-services` and utilize those privileges for nefarious purposes. The services that run under the `vx-services` user account offer their services over local HTTP, with well-formed semantics as to what actions they allow. The authentication status is checked on the backend, by `vx-services`, so actions can only be taken if a valid authentication session is open.

Meanwhile, if a user were to break out of the constraints we've placed on the window manager and obtain a shell, that shell would run as `vx-ui`, which as the ability to call into services run as `vx-services`, but does not itself have the direct privileges of `vx-services`. Thus, an attacker that penetrates the first line of defense would remain severely thwarted in what they can do next.
