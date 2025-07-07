# Reliably Detectable Marks

Marks are determined valid and counted by the system if the amount of darker pixels in the bubble area exceeds a configurable "definite" mark threshold set in the [election-package](../system-overview/election-package/ "mention") system settings file. This mark threshold can be adjusted to have a stricter or looser interpretation of what is considered a valid mark. On both VxScan and VxCentralScan, the voting system does not process any marks as ambiguous. All marks are either valid or invalid.

The recommended and default threshold is 7%. With this threshold setting, hand marked paper ballot interpretation detects a valid mark per the mark conditions described by VVSG 1.1.6-H.

At this default threshold, marks such as a light dot, a fold through a bubble, a stray mark outside of the bubble, or a small line just on the corner of a bubble will be considered invalid. Marks such as a completely filled bubble, half filled bubble, or an X in a bubble will be considered valid.

Examples of invalid and valid marks along with the score for that mark (in green) are shown below.&#x20;

The mark threshold set on a scanner can be checked by an election official at any point by viewing the readiness report for that device as described in [diagnostics.md](../system-overview/diagnostics.md "mention") (see also [VxScan Diagnostics](https://app.gitbook.com/s/JtZutzGTdCzsGITrdiph/vxscan/vxscan-diagnostics "mention") & [VxCentralScan Diagnostics](https://app.gitbook.com/s/JtZutzGTdCzsGITrdiph/vxcentralscan/vxcentralscan-diagnostics "mention") in the user manual).

### Invalid Marks

<figure><img src="../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

### Valid Marks

<figure><img src="../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>

### Marginal Marks

The system also support setting a marginal mark threshold, for flagging ambiguous marks close to but note quite over the definite mark threshold. If a marginal mark threshold is set and marginal mark adjudication is enabled, the definite mark threshold can be increased without having to worry about completely missing marks.

