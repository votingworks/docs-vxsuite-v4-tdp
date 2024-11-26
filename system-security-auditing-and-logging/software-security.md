---
description: >-
  This section describe the overall system security architecture of VxSuite and
  the measures taken to thwart attacks on the proper operation of elections on
  VxSuite.
---

# System Security Architecture

{% hint style="success" %}
**Requirement 14.1-C.1** – the use of **cryptography** to secure VxSuite – is covered in the following sections:

* [Access Control](system-security-architecture/access-control.md) describes the certificates and signatures used by smart cards.
* [Artifact Authentication](system-security-architecture/artifact-authentication/) describes the signatures applied to all files exchanged between system components.
* [System Integrity](system-security-architecture/system-integrity.md) describes the hard-drive partition hashes and the kernel and bootloader signature used by Secure Boot.
* [Cryptography](system-security-architecture/cryptography.md) provides additional details on encryption vs. authentication and the type and size of cryptographic keys that we use.
{% endhint %}

{% hint style="success" %}
**Requirement 14.1-C.2** – the use of **malware protection** to secure VxSuite – is covered by Secure Boot and safe mounting of external drives, described in [System Integrity](system-security-architecture/system-integrity.md).
{% endhint %}

{% hint style="success" %}
**Requirement 14.1-C.3** – the use of **a firewall** to secure VxSuite – is covered in [Networking](system-security-architecture/networking.md).
{% endhint %}

{% hint style="success" %}
**Requirement 14.1-C.4** – the use of **system configurations** to secure VxSuite – is covered in [Password and Credential Policies](system-security-architecture/password-and-credential-policies.md) and [System Integrity](system-security-architecture/system-integrity.md).
{% endhint %}

{% hint style="success" %}
**Requirement 11.4-A** – on **least privilege** – is covered in [Defense in Depth and Least Privilege](system-security-architecture/defense-in-depth-and-least-privilege.md).
{% endhint %}

{% hint style="success" %}
**Requirements 13.3-A, 13.3-C, 13.3-D** are covered in [Cryptography](system-security-architecture/cryptography.md).
{% endhint %}

