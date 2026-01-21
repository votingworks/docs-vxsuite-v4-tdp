# System Limits

## Election Definition Limits

| Limit Type    | Per                     | Value  |
| ------------- | ----------------------- | ------ |
| Precincts     | Election                | 1,000  |
| Candidates    | Election                | 1,000  |
| Contests      | Election                | 1,000  |
| Ballot Styles | Election                | 1,000  |
| Candidates    | Contest                 | 100    |
| Vote For      | Contest                 | 50     |
| Characters    | Name, Title, Label      | 100    |
| Characters    | Proposition Description | 10,000 |

## Component Limits

### VxAdmin

* The total number of CVRs that can be imported is limited by the total disk space on the laptop (\~200GB). The exact number of CVRs depends ballot size, ballot selections, tabulator used (VxScan or VxCentralScan), and other factors that determine expected CVR size.

### VxCentralScan

* The total number of ballots scanned is limited by the total disk space on the laptop (\~200GB). The exact number of ballots depends on ballot size, complexity, and selections made that influence determine the CVR and ballot image sizes.
* VxCentralScan is limited by the batch scanner maximum tabulation rate: [maximum-tabulation-rate.md](maximum-tabulation-rate.md "mention")

### VxMarkScan

* VxMarkScan only supports 8" x 11" and 8" x 13.25" ballot sizes as specified in [paper-ballot-specifications.md](../paper-ballot-specifications.md "mention").&#x20;
* VxMarkScan ballot styles are limited to 25 contests.
* A contest allows voting for **n** out of **m** candidates/choices. The general limits for **n** and **m** are listed in the above table: **n** = _Vote For_ per _Contest_ and **m** = _Candidates_ per _Contest_.
  * On VxMarkScan, for any one contest, **n** is limited to 25 (lower than the general limit), and **m** is limited to 100 (the same as the general limit).
  * Take the sum of **n** across all contests on a ballot style to be **N** and the sum of **m** across all contests on a ballot style to be **M**. On VxMarkScan, **N** is limited to 75, and **M** is limited to 135.
* Each VxMarkScan write-in is limited to 40 characters. The sum of write-in characters across all contests on a VxMarkScan ballot is limited to 60.
* The ballot box supports up to 200 ballots before needing to be cleared.
* VxMarkScan can activate, mark, verify, and cast up to 20 ballots per hour. Exact rate depends on time spent by user marking and verifying a ballot before casting.
* VxMarkScan has a maximum available disk space of 9GB.

### VxScan

* The ballot box supports up to 3000 ballots in the main compartment before needing to be cleared.
* The ballot box auxiliary compartment supports up to 100 ballots before needing to be cleared. Ballots longer than 19" must be folded.
* Total ballots scanned for a given VxScan configuration are limited to 10,000 ballots. This limit is set based on the disk space available on specified external disks to ensure adequate disk space in the case of needing to re-sync CVRs.
* Ballot tabulation rate depends on election content / ballot length. A typical 11" ballot sheet is scanned and tabulated in 3 seconds.
* An user can feed a ballot sheet every 10 seconds. At that feeding rate, the maximum tabulation rate is 360 sheets per hour.

### Hand Marked Paper Ballots

In addition to the design requirements specified in [hand-marked-ballots.md](../../system-overview/hand-marked-ballots.md "mention"), ballots are constrained by the following limits.

#### Bubble Positions

VxSuite hand marked paper ballot interpretation supports fractional grid coordinate positions, which enable bubble positions to be placed anywhere within the timing mark grid. However, the density of bubbles on a given ballot is limited to the total number of timing mark grid intersections to ensure accurate interpretation.

For example, an 11" ballot has a 32 x 39 timing mark grid. The QR code and the footer typically occupy the bottom two rows of bubbles so the usable grid is 32 x 37, giving a maximum number of ballot positions of 1,184 per page or 2,368 per sheet. The maximum number of ballot positions increases for longer ballots due to the longer grid.

**Candidates Per Contest**

The total number of candidates per contest is limited by ballot design requirements restricting contest options to one column and one page (7.3-B.1). Therefore, the maximum number of candidates in a contest is the maximum number of bubble positions in a column. For a 22" ballot, there is a maximum of 83 possible bubble positions in a column. The maximum number of candidates per contest may be lower than 83 when accounting for instructional text and contest information in the ballot design.
