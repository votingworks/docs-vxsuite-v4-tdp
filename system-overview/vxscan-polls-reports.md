# VxScan Polls Reports

## Polls Opened and Closed Reports

When polls open or close on VxScan, a tally report is printed. The tally report contains the tally results (pre-adjudication) of all ballots scanned at the scanner.

The tally report header contains the following information:

* **Title** - Includes the type of the polls report and the name of the precinct, or "All Precincts" if VxScan is configured to accept ballots from all precincts
* **Subtitle** - For primary elections, includes the full party name or "Nonpartisan Contests"
* **Election Info** - The title, date, and location of the election
* **Timestamps** - The first timestamp indicates when the poll status changed and the second indicates when the report was printed. In most cases these times are the same, but in some cases the report may be printed later.
* **Election ID** - The election ID on the report is a concatenation of the ballot hash and election hash and specifies exactly which election definition and election settings that the report corresponds to
* **Certification Signatures** - The space is provided for poll workers or election officials to sign the report in accordance with local statute.

The ballot counts table provides the count of hand marked vs. machine marked ballots. For elections with multi-sheet ballots, it provides counts per sheet.

Each candidate or contest option appears in a row below the contest header. Because results at VxScan are not yet adjudicated, all write-ins are grouped under the "Write-In" bucket (except unmarked write-ins, which are reported as undervotes until adjudicated at VxAdmin).

As a rule, the sum of the number of votes for all candidates, the number of undervotes, and the number of overvotes will equal the number of total possible votes for the contest, which is the number of ballots times the number of selections allowed.

<pre><code><strong>candidate votes + undervotes + overvotes = ballots * votes allowed
</strong></code></pre>

<div><figure><img src="../.gitbook/assets/image (70).png" alt="" width="375"><figcaption><p>Party-specific portion of a polls opened report for a primary</p></figcaption></figure> <figure><img src="../.gitbook/assets/image (72).png" alt="" width="375"><figcaption><p>Polls closed report for a general election in test ballot mode</p></figcaption></figure></div>

## Polls Paused and Resumed Reports

When voting is paused or resumed, VxScan prints a report containing the ballot count. Tally results are never included. The header is structured in the same way as the polls opened and closed reports.

<div><figure><img src="../.gitbook/assets/image (74).png" alt="" width="375"><figcaption><p>Voting paused report</p></figcaption></figure> <figure><img src="../.gitbook/assets/image (75).png" alt="" width="375"><figcaption><p>Voting resumed report</p></figcaption></figure></div>
