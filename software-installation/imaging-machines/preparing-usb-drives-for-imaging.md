# Preparing USB Drives for Imaging

To install an image on a VotingWorks component, i.e., to image a machine, you need two USB drives:

* A vx-iso USB drive — [vx-iso](https://github.com/votingworks/vx-iso) is an Arch Linux ISO installer program.
* An image USB drive — This is an empty USB drive, partitioned in a particular way, with a "Data" partition that can contain as many VotingWorks images as space allows and a "Keys" partition that can optionally contain the VotingWorks Secure Boot public keys, necessary if these keys haven't already been installed.

Clone the vx-iso repo for the tooling necessary to prepare the above:

```
git clone https://github.com/votingworks/vx-iso.git
cd vx-iso
```

To create a vx-iso USB drive, you can follow these instructions: [https://github.com/votingworks/vx-iso/blob/main/README.md#creating-an-install-drive](https://github.com/votingworks/vx-iso/blob/main/README.md#creating-an-install-drive)

{% hint style="info" %}
If this is SLI, we have provided you with vx-iso USB drives so that you don't need to prepare them from scratch.
{% endhint %}

To create an image USB drive, you can follow these instructions: [https://github.com/votingworks/vx-iso/blob/main/README.md#creating-an-image-with-optional-secure-boot-keys-drive](https://github.com/votingworks/vx-iso/blob/main/README.md#creating-an-image-with-optional-secure-boot-keys-drive)

You'll need access to the relevant images and optionally the VotingWorks Secure Boot **public** keys. Both of these are stored on a private S3 bucket, though they're not sensitive, and VotingWorks can prepare temporary links to grant access to them.

{% hint style="info" %}
If this is SLI, you do not need to create data drives with the VotingWorks Secure Boot public keys. Secure Boot has already been configured on all your machines.
{% endhint %}



