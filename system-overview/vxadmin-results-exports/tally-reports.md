# Tally Reports

## Basic Structure

The basic structure of the tally reports printed from VxAdmin is similar to the [polls opened and closed reports](../vxscan-polls-reports.md) printed from VxScan.

<figure><img src="../../.gitbook/assets/image (76).png" alt="" width="375"><figcaption><p>Full election tally report</p></figcaption></figure>

## Filtered and Grouped Reports

In addition to the full election report, VxAdmin exports reports filtered or grouped by the following dimensions:

* Ballot Style
* Precinct
* Voting Method
* Scanner
* Batch
* District (filtering only)

When a report is grouped, the report is broken up into multiple sections each with their own filter. For example, if you were to group by "Voting Method," the resulting report would have a section filtered for precinct ballots only and a section filtered for absentee ballots only:

<div><figure><img src="../../.gitbook/assets/image (77).png" alt="" width="375"><figcaption><p>First part of a grouped tally report</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (78).png" alt="" width="375"><figcaption><p>Second part of a grouped tally report</p></figcaption></figure></div>

The filter for a given report section is indicated in the title of the report. If the report has more than one filter applied to it, the full details of the filter will be specified in a box below the title:

<figure><img src="../../.gitbook/assets/image (86).png" alt="" width="375"><figcaption><p>Tally report with a complex filter</p></figcaption></figure>

Note that filters and groups can be combined.

## Manual Results

If manual results have been added, they will be included in the tally report alongside the scanned results. For each contest, there will be three results columns: "scanned", "manual", and "total".

<figure><img src="../../.gitbook/assets/image (80).png" alt="" width="375"><figcaption><p>Tally report with manual results</p></figcaption></figure>

## Write-In Candidate Aggregation

In order to prevent a long list of write-in candidates from making contest results difficult to read, VxAdmin tally reports consolidate write-in candidates if they're not relevant to the contest outcome. Relevant write-ins are included as "\<Name> (Write-In)". Irrelevant write-ins are consolidated as "Write-In" or, if there are relevant write-ins in the list, "Other Write-In". Unadjudicated write-ins are always consolidated as "Unadjudicated Write-In."

A write-in is deemed relevant if it must be listed for the reader to determine the winner(s) of the contest. In the middle example below, the single adjudicated write-in is consolidated because _Natalie Portman_ is the winner regardless of the identities of the write-ins. In the last example, however, there are 31 adjudicated write-ins so it's possible that a write-in got more votes than _Natalie Portman_. The report then enumerates the write-ins with the highest vote totals until the "Other Write-In" count is smaller than the counts for all winners.&#x20;

<div><figure><img src="../../.gitbook/assets/Screen Shot 2024-10-01 at 4.52.26 PM.png" alt="" width="407"><figcaption><p>Before adjudication</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Screen Shot 2024-10-01 at 4.52.31 PM.png" alt="" width="392"><figcaption><p>Adjudication just started</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Screen Shot 2024-10-01 at 4.52.45 PM.png" alt="" width="399"><figcaption><p>Adjudication almost finished</p></figcaption></figure></div>

