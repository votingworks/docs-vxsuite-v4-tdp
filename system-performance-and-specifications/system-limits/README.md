# System Limits

## Election Definition Limits

| Limit Type    | Per        | Value |
| ------------- | ---------- | ----- |
| Precincts     | Election   | 1000  |
| Candidates    | Election   | 1000  |
| Contests      | Election   | 1000  |
| Ballot Styles | Election   | 1000  |
| Candidates    | Contest    | 100   |
| Vote For      | Contest    | 50    |
| Characters    | Field Name | 100   |

## Component Limits

### VxAdmin

* The total number of CVRs that can be imported is limited by the total disk space on the laptop (\~200GB). The exact number of CVRs depends ballot size, ballot selections, tabulator used (VxScan or VxCentralScan), and other factors that determine expected CVR size.

### VxCentralScan

* The total number of ballots scanned is limited by the total disk space on the laptop (\~200GB). The exact number of ballots depends on ballot size, complexity, and selections made that influence determine the CVR and ballot image sizes.
* VxCentralScan is limited by the batch scanner maximum tabulation rate: [maximum-tabulation-rate.md](maximum-tabulation-rate.md "mention")

### VxMark

* VxMark only supports 8" x 13.25" ballots as specified in [paper-specifications.md](../paper-specifications.md "mention").
* VxMark is limited to printing of 50 contest selections before needing to reduce text size to fit a summary ballot on a single sheet. VxMark can print a maximum of 100 contest selections with text-size reduction.

### VxScan

* The ballot box supports up to 3000 ballots cast in the main compartment before needing to be cleared.
* The ballot box auxiliary compartment supports up to 100 ballots cast before needing to be cleared. Ballots longer than 19" must be folded.
* Total ballots scanned for a given VxScan configuration are limited to 10,000 ballots. This limit is set based on the disk space available on specified external disks to ensure adequate disk space in the case of needing to re-sync CVRs.

### Hand Marked Paper Ballots

VxSuite hand marked paper ballot interpretation supports fractional grid coordinate positions, which enable bubble positions to be placed anywhere within the timing mark grid. However, the density of bubbles on a given ballot is limited to the total number of timing mark grid intersections to ensure accurate interpretation.

For an 11" ballot, which has a 32 x 39 timing mark grid, the maximum number of ballot positions is 1248 per page or 2496 per sheet. The maximum number of ballot positions increases for longer ballots due to the longer grid.













