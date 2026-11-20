# Basic Configuration Wizard

If this is the first time that a VotingWorks application has been installed to a machine, the machine boots into a basic configuration wizard. If the machine has been previously configured with a certified VotingWorks application of the same type, this wizard is skipped.

Most of the steps are self-explanatory; "Step 1: Set Machine ID" and "Step 4: Create Machine Cert" are explained below.

## Setting Machine ID

The machine ID must be unique for each machine. Many machines have a physical placard on them indicating the machine ID. Use that ID here.

## Creating Machine Cert

On VxAdmin, the wizard first prompts for a jurisdiction:

{% code overflow="wrap" %}
```
Enter a jurisdiction ({state-2-letter-abbreviation}.{county-town-etc}, e.g., ca.los-angeles or vx.test for test/demo machines):
```
{% endcode %}

{% hint style="info" %}
SLI should use `co.sli`.
{% endhint %}

Then, on all machines, the wizard displays this prompt:

{% code overflow="wrap" %}
```
Insert a USB drive into the machine. Press enter once you've done so.
```
{% endcode %}

Insert a USB drive designated for this purpose, referred to below as the VxCertifier USB drive.

After the VxCertifier USB drive is inserted, a certificate signing request is written to it, and the wizard displays this prompt:

{% code overflow="wrap" %}
```
Remove the USB drive, take it to VxCertifier, and bring it back to this machine when prompted. Press enter once you've re-inserted the USB drive.
```
{% endcode %}

Because the machine is certified at a facility other than a VotingWorks facility, the USB drive cannot be taken to VxCertifier, the VotingWorks certification terminal. Use the following remote certification process instead:

1. Remove the VxCertifier USB drive and find the `csr-<machine-id>.pem` file inside the `certs/` directory on it.
2. Share that file with VotingWorks. This file does not contain any private information, so it can be shared over the internet, e.g., via email.
3. Wait for VotingWorks to prepare a certificate from this file and send it back as a `cert-<machine-id>.pem` file. This file also does not contain any private information, so it can be shared over the internet.
4. Copy the `cert-<machine-id>.pem` file onto the VxCertifier USB drive, in the same `certs/` directory that contained the `csr-<machine-id>.pem` file.
5. Re-insert the USB drive into the machine and press Enter. The wizard continues.

On VxAdmin, the last step is to program the first system administrator card. Record the displayed PIN. On other machines, no steps remain. The machine then reboots into the application.
