# Basic Configuration Wizard

After you've imaged a machine, the machine will boot into a basic configuration wizard. The majority of the steps are self-explanatory, but "Step 1: Set Machine ID" and "Step 4: Create Machine Cert" require some extra clarification.

### Setting Machine ID

It is important that the machine ID be unique for each machine. Many machines have a physical placard on them indicating the machine ID. That is the ID that should be used here.

### Creating Machine Cert

On VxAdmin, you'll first see a prompt to enter a jurisdiction:

{% code overflow="wrap" %}
```
Enter a jurisdiction ({state-2-letter-abbreviation}.{county-town-etc}, e.g., ca.los-angeles or vx.test for test/demo machines):
```
{% endcode %}

{% hint style="info" %}
SLI should use co.sli
{% endhint %}

Then, on all machines, you'll see this prompt:

{% code overflow="wrap" %}
```
Insert a USB drive into the machine. Press enter once you've done so.
```
{% endcode %}

Insert a USB drive that you designate for this purpose. From here on out, we'll refer to this USB drive as the VxCertifier USB drive.

After selecting the VxCertifier USB drive, a certificate signing request will be written to it. You'll then be prompted to:

{% code overflow="wrap" %}
```
Remove the USB drive, take it to VxCertifier, and bring it back to this machine when prompted. Press enter once you've re-inserted the USB drive.
```
{% endcode %}

Because you'll be certifying your machine at your own facility as opposed to a VotingWorks facility, you won't be able to take the USB to VxCertifier, our VotingWorks certification terminal. We'll need to use a remote certification process instead.

You'll need to remove the USB drive, find the "csr.pem" file inside the "certs/" directory on the USB drive, and share that file with VotingWorks. This file does not contain any private information so can be shared over the internet, e.g., via email. VotingWorks will prepare a certificate given this "csr.pem" file and send the certificate back to you, in the form of a "cert.pem" file. This file, too, does not contain any private information so can be shared over the internet. You'll need to copy this "cert.pem" file back onto the USB that you started with, placing it in the same USB drive's "certs/" directory. Re-inserting this USB into the machine and pressing enter should allow you to proceed successfully.

On VxAdmin, you'll be prompted to program your first system administrator card as a last step. Remember to record the displayed PIN. On other machines, no steps remain! You'll reboot into the app after this.
