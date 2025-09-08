# System Overview



<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption><p>Top level system diagram</p></figcaption></figure>

The VotingWorks voting system (a.k.a. **VxSuite**) consists of four primary components:&#x20;

* **VxAdmin**: election setup and election results manager
* **VxMarkScan**: ballot-marking device (BMD)
* **VxScan**: precinct scanner
* **VxCentralScan**: batch scanner

Voters mark paper ballots by [hand](system-overview/hand-marked-ballots.md) or by using VxMarkScan to [machine mark](system-overview/machine-marked-ballots.md). Ballots are read and counted by tabulating devices (VxScan & VxCentralScan), which create [cast vote records](system-overview/cast-vote-records.md) for adjudication and aggregation on VxAdmin.

An election begins with generating an [election package](system-overview/election-package/) and [hand marked ballots ](system-overview/hand-marked-ballots.md)using an external system.

## VxAdmin

VxAdmin is where the election administrator performs election setup tasks and manages election results. At the beginning of an election, the user configures VxAdmin with an [election package](system-overview/election-package/). Once configured, VxAdmin is used for two key election setup tasks:

* Exporting a copy of the election package to USB drives with a [digital signature](system-security-auditing-and-logging/system-security-architecture/artifact-authentication/). The election package is used to configure VxMarkScan, VxScan, and VxCentralScan, and it _must_ be digitally signed by VxAdmin.
* Programming [role-based smart cards](system-overview/user-roles.md) that will be used to authenticate on all machines. While the "System Administrator" role is election-agnostic, the "Election Manager" and "Poll Worker" roles are election-specific and cards must be programmed for every election.

VxAdmin is later used to load, store, and aggregate cast vote records from the scanners. The results are available for review or export in [several results formats](system-overview/vxadmin-results-exports/). Election administrators can mark results as official, after which no new results can be added.

* [vxadmin-function.md](system-overview/vxadmin-function.md "mention")
* [vxadmin-and-vxcentralscan-hardware.md](system-overview/vxadmin-and-vxcentralscan-hardware.md "mention")

## VxMarkScan

VxMarkScan is the system's ballot-marking device (BMD) that provides an accessible voting experience. At the beginning of an election, it is configured with an [election package](system-overview/election-package/) from VxAdmin. Once configured, a voter can make vote selections in various interaction modes according to their needs.

The following input modes are supported:

* Touch, using the touchscreen
* Tactile, using the accessible controller
* Limited Dexterity, using a sip-and-puff device or other dual-switch input

The following output modes are supported:

* Visual, with options to change color contrast and text size
* Audio, with navigation instructions and contest details read to the user over headphones

The voter can also adjust the language based on translations included in the election package.&#x20;

After the voter finishes their vote selections, VxMarkScan prints a [machine marked ballot](system-overview/machine-marked-ballots.md) and presents it to the voter. The ballot is scanned (but not cast) so the interpreted results can be presented to the voter on-screen. After reviewing the ballot and confirming their selections, the ballot is cast and ejected into the attached ballot box. At a later time, depending on election procedures, the ballot will be removed from the ballot box for tabulation.

* [vxmark-function.md](system-overview/vxmark-function.md "mention")
* [vxmark-hardware.md](system-overview/vxmark-hardware.md "mention")

## VxScan

VxScan is the system's precinct scanner. At the beginning of an election, it is configured with an [election package](system-overview/election-package/) from VxAdmin. The election package specifies the ballot layouts. The polls are opened by a poll worker after which casting ballots is allowed. Opening polls prints [a tally report](system-overview/vxscan-polls-reports.md) which is empty because no ballots have been scanned, a.k.a. the zero report.&#x20;

Voters cast ballots by inserting their ballots into the scanner in any orientation. After interpreting the scanned ballot, the scanner will drop the ballot into the ballot box and inform the voter that their ballot was successfully cast. During voting, VxScan continuously exports [cast vote records](system-overview/cast-vote-records.md) to an attached USB drive.

If the election is [configured to support second-chance voting](system-overview/election-package/#system-settings) and the ballot triggers a configured adjudication reason (e.g. it has an overvote), the scanner will hold the ballot while the voter is notified of the issues on their ballot. The voter then chooses whether to cast their ballot or return it to update or spoil.

When polls are closed, the CVR export is completed and a [polls closed report ](system-overview/vxscan-polls-reports.md)prints. The polls closed report includes the vote tallies of all ballots cast at the scanner while polls were open. Unlike the vote tallies eventually exported from VxAdmin, the vote tallies at VxScan do not contain any post-voting adjudication information such as write-in adjudication. The CVR export on the USB drive is then taken to VxAdmin for adjudication, aggregation, and reporting.

* [vxscan-function.md](system-overview/vxscan-function.md "mention")
* [vxscan-hardware.md](system-overview/vxscan-hardware.md "mention")

## VxCentralScan

VxCentralScan is the system's batch scanner, often used to scan absentee or provisional ballots. At the beginning of an election, it is configured with an [election package](system-overview/election-package/) from VxAdmin. The election package specifies the ballot layouts.

Ballots are inserted in the batch scanner's hopper and a batch scan is triggered from VxCentralScan. The ballots are scanned and interpreted in succession until the hopper is empty. If a ballot triggers a configured adjudication reason (e.g. it has an overvote), scanning will pause and the ballot will be displayed on screen, at which point the user can choose to tabulate the ballot anyway or remove it, untabulated.

After scanning is complete, the user can export the [cast vote records](system-overview/cast-vote-records.md) to a USB drive and take the USB drive to VxAdmin for adjudication, aggregation, and reporting.

* [vxcentralscan-function.md](system-overview/vxcentralscan-function.md "mention")
* [vxadmin-and-vxcentralscan-hardware.md](system-overview/vxadmin-and-vxcentralscan-hardware.md "mention")
