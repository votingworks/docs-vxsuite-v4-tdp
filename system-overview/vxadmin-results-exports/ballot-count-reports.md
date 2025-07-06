# Ballot Count Reports

Ballot count reports contain ballot and ballot sheet counts, not contest results.

The ballot counts are broken down by ballot type - "HMPB" (for hand marked ballots), "BMD" (for machine marked ballots), and "manual" (for manually entered results, if applicable).

If there are multi-sheet ballots, the hand marked ballot counts may have sheet counts specified. The ballot count is determined by counting the first sheet of each ballot style.

When grouping is applied in a ballot count report, each group corresponds to a row in the table. In the following example, the ballot counts are grouped by both precinct and voting method:

<figure><img src="../../.gitbook/assets/image (81).png" alt="" width="375"><figcaption><p>Ballot count report</p></figcaption></figure>

The following metadata columns may appear in a ballot count report table in order to specify groupings:

<table><thead><tr><th width="177">Header</th><th>Values</th></tr></thead><tbody><tr><td>Precinct</td><td>The name of the precinct</td></tr><tr><td>Ballot Style</td><td>The internal identifier of the ballot style</td></tr><tr><td>Party</td><td>The short name of the party, e.g. "Democrat". Included by default if the ballot style is included, in a primary</td></tr><tr><td>Voting Method</td><td>"Precinct", "Absentee", or "Provisional"</td></tr><tr><td>Scanner ID</td><td>The serial number of the scanner. Included by default if the batch is included</td></tr><tr><td>Batch</td><td>The label for the batch, or "Manual Tallies" for manually entered data</td></tr></tbody></table>

Filters apply to the entire report. Simple filters are shown in the title, while complex filters are listed in a box below the title.

<figure><img src="../../.gitbook/assets/image (83).png" alt="" width="375"><figcaption><p>Ballot count report with a complex filter</p></figcaption></figure>
