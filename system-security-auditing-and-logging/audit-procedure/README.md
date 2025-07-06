---
description: >-
  VxSuite can be audited using post-election audits, including a
  ballot-comparison or batch-comparison risk-limiting audit, or an image audit.
---

# Audit Procedure

## Ballot-Comparison Risk-Limiting Audit

In a **ballot-comparison risk-limiting audit**, the goal is to compare, for a random sample of the cast ballots, the paper ballot and the corresponding cast-vote record. The specifics of sample selection and risk-limit calculation are out of scope for this document – VotingWorks Arlo or other RLA tool may be used for this purpose.

To enable a ballot-comparison risk-limiting audit, VxSuite provides:

* imprinting of ballots on VxCentralScan, with a unique identifier of the form\
  `<BATCH-ID>_<SEQUENCE-NUM>`
* cast-vote records including the field `BallotAuditId` which matches the imprinted identifier

Then, to run a ballot-comparison risk-limiting audit with VxSuite:

1. scan all ballots with VxCentralScan and the imprinter module on the Ricoh scanner. See [#imprinting](../../system-overview/vxcentralscan-function.md#imprinting "mention").
2. store ballots by batch, recording the batch ID displayed on VxCentralScan display. Storing ballots in the order they were scanned is helpful for later retrieval, but not strictly necessary since the sequence numbers printed on the ballots can be used to recover the proper order.
3. export CVRs from all the VxCentralScan's
4. use VxAdmin to aggregate CVRs, adjudicate write-ins, and generate final tallies
5. aggregate tallies and CVRs at the audit jurisdiction level, most often the State
6. input the CVRs and tallies into a risk-limiting audit tool
7. the RLA tool will generate a sample of ballots to audit
8. retrieve the selected ballots by batch ID and sequence number
9. enter the interpretation of those ballots into the RLA tool
10. the RLA tool will either declare the audit successful or require an escalation. The RLA tool will ultimately declare the election a success or call into question how ballots were interpreted.

Alternatively, unique identifiers may be added by VxScan — see [vxscan-unique-identifiers.md](vxscan-unique-identifiers.md "mention")for the associated audit procedure.

## Batch-Comparison Risk-Limiting Audit

In a **batch-comparison risk-limiting audit**, the goal is to compare, for a random sample of ballot batches, the hand tally of that batch with the corresponding batch tally. The specifics of sample selection and risk-limit calculation are out of scope for this document – VotingWorks Arlo or other RLA tool may be used for this purpose.

To enable a batch-comparison risk-limiting audit, VxSuite provides:

* Tallies partitioned by scanner and/or by batch in VxAdmin
* Ballot counts by scanner and by batch in VxAdmin

Then, to run a batch-comparison risk-limiting audit with VxSuite:

1. scan ballots either with VxScan or VxCentralScan. No need to use imprinting for VxCentralScan.
2. store ballots by batch – where a batch in VxCentralScan is indicated by the batch ID on screen, and a batch in VxScan is the entire set of ballots scanned by a single VxScan over the course of the election. Order of the ballots need not be maintained in either case.
3. export CVRs from all VxCentralScans and gather the CVRs on USB drives from all VxScans
4. use VxAdmin to aggregate CVRs, adjudicate write-ins, and generate final tallies
5. produce ballot counts by scanner and by batch on VxAdmin – these are effectively contest totals by batch files in auditing language.
6. aggregate tallies and ballot manifests at the audit jurisdiction level, most often the State.
7. input tallies and ballot manifests into the RLA tool
8. the RLA tool will generate a sample of batches to audit
9. retrieve the batches and recount them by hand – usually only for one or two contests, as directed by the audit procedure
10. enter the hand-count batch tallies into the RLA tool
11. the RLA tool will either declare the audit successful or require an escalation. The RLA tool will ultimately declare the election a success or call into question how ballots were interpreted.

## Image Audits

In an **image audit**, various risk-limiting audit procedures are used, but instead of physically retrieving the ballots to audit, the scanned image of the ballot is used.

VxSuite supports image audits very simply – every VxScan and VxCentralScan produces images of the scanned ballots that can be immediately associated with the interpreted CVR. Thus, the protocols defined above for ballot-comparison and batch-comparison audits can be used, with the following simplification:

* imprinting is unnecessary
* instead of "retrieving a ballot", simply look up the image files corresponding to the CVR ID and interpret on screen

