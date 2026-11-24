# Reliably Detectable Marks

Marks are determined valid and counted by the system if the amount of darker pixels in the bubble area exceeds a configurable "definite" mark threshold set in the [election-package](../system-overview/election-package/ "mention") system settings file. This mark threshold can be adjusted to have a stricter or looser interpretation of what is considered a valid mark. On both VxScan and VxCentralScan, a mark is either valid or invalid unless a marginal mark threshold is also set. In that case, a mark between the marginal and definite mark thresholds is a marginal mark (an ambiguous mark in VVSG 2.0 terms) and can be flagged for adjudication; see [Marginal Marks](#marginal-marks).

The recommended definite mark threshold is 7%. With this threshold setting, bubble ballot interpretation detects a valid mark per the mark conditions described by VVSG 2.0 1.1.6-H.

At this threshold, marks such as a light dot, a fold through a bubble, a stray mark outside of the bubble, or a small line just on the corner of a bubble are considered invalid. Marks such as a completely filled bubble, half filled bubble, or an X in a bubble are considered valid.

Examples of invalid and valid marks along with the score for that mark (in teal, below each bubble) are shown below.

The mark threshold set on a scanner can be checked by an election official at any point by viewing the readiness report for that device as described in [diagnostics.md](../system-overview/diagnostics.md "mention") (see also [VxScan Diagnostics](https://app.gitbook.com/s/Blk9V7L3xSoGDrocz6MA/vxscan/vxscan-diagnostics "mention") and [VxCentralScan Diagnostics](https://app.gitbook.com/s/Blk9V7L3xSoGDrocz6MA/vxcentralscan/vxcentralscan-diagnostics "mention") in the user manual).

## Invalid Marks

<figure><img src="../.gitbook/assets/image (65).png" alt="Scanned bubble crops of invalid marks (dots, circled names, stray lines) with mark scores below 7%"><figcaption></figcaption></figure>

## Valid Marks

<figure><img src="../.gitbook/assets/image (1) (2).png" alt="Scanned bubble crops of valid marks (filled, half-filled and X marks) with mark scores above 7%"><figcaption></figcaption></figure>

## Marginal Marks

The system also supports setting a marginal mark threshold for flagging ambiguous marks close to but not quite over the definite mark threshold. If a marginal mark threshold is set and marginal mark adjudication is enabled, the definite mark threshold can be increased while marks that fall just below it are flagged for adjudication rather than missed.

