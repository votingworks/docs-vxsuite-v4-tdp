# Ballot Count Reports

Ballot count reports contain ballot and ballot sheet counts, not contest results.

If there are multi-sheet ballots in the election, the sheet counts (e.g. "Sheet 1", "Sheet 2") can be added to the report in the ballot count report builder by selecting "Sheet" as a `Report By` dimension. The total ballot count is always defined as the first sheet count.

If there are manual results, the manual ballot count will always be displayed separately from the scanned ballot count, and the total of the two will also be displayed.

When grouping is applied in a ballot count report, each group corresponds to a row in the table. In the following example, the ballot counts are grouped by both precinct and voting method:

<figure><img src="../../.gitbook/assets/ballot-count-report-1.png" alt="" width="375"><figcaption><p>Ballot count report</p></figcaption></figure>

The following metadata columns may appear in a ballot count report table in order to specify groupings:

<table><thead><tr><th width="177">Header</th><th>Values</th></tr></thead><tbody><tr><td>Precinct</td><td>The name of the precinct</td></tr><tr><td>Ballot Style</td><td>The internal identifier of the ballot style</td></tr><tr><td>Party</td><td>The short name of the party, e.g. "Democrat". Included by default if the ballot style is included, in a primary</td></tr><tr><td>Voting Method</td><td>"Precinct", "Absentee", or "Provisional"</td></tr><tr><td>Scanner ID</td><td>The serial number of the scanner. Included by default if the batch is included</td></tr><tr><td>Batch</td><td>The label for the batch, or "Manual Tallies" for manually entered data</td></tr></tbody></table>

Filters apply to the entire report. Simple filters are shown in the title, while complex filters are listed in a box below the title.

<figure><img src="../../.gitbook/assets/ballot-count-report-complex-filter-1.png" alt="" width="375"><figcaption><p>Ballot count report with a complex filter</p></figcaption></figure>
