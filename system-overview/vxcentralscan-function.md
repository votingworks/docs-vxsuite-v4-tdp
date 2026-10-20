# VxCentralScan Function

VxCentralScan is the system's batch scanner which allows efficiently scanning large batches of ballots.

## Configuration

VxCentralScan is configured with a signed [election-package](election-package/ "mention") exported from VxAdmin. The election definition includes the ballot layouts necessary for interpreting ballots and the system settings which indicate what type of ballot issues (e.g. overvotes) require adjudication. After the election package is loaded by an authenticated election manager, VxCentralScan's polling place is configured. If the election has exactly one absentee polling place, VxCentralScan selects it automatically and no further action is required; otherwise the election manager must select a polling place before scanning. The selected polling place determines which ballots VxCentralScan will accept: ballots outside it cause VxCentralScan to stop and refuse to tabulate them (see [Ballot Issues & Adjudication](vxcentralscan-function.md#ballot-issues-and-adjudication)). The polling place cannot be changed once ballots have been scanned.

{% hint style="info" %}
**User Manual Reference:** [Configure VxCentralScan](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxcentralscan/configure-ballot-scanner "mention")
{% endhint %}

### Ballot Mode

After initial configuration, VxCentralScan is in test ballot mode. The election manager can toggle between test ballot mode and official ballot mode. In official ballot mode, only official ballots can be scanned and exported CVRs will be official ballot CVRs. In test ballot mode, only test ballots can be scanned and exported CVRs will be test ballot CVRs. If `allowOfficialBallotsInTestMode` is set in the [system settings](election-package/#system-settings), official ballots will be allowed in test mode but exported CVRs will still be test CVRs.

Switching between ballot modes clears all scanned ballot data. The election manager can switch from test ballot mode to official ballot mode at any time. When in official ballot mode after ballots have been scanned, the election manager can only switch back to test ballot mode if the scanned ballot data has been backed up.

### Unconfiguring

VxCentralScan can be unconfigured by an election manager or system administrator. If ballots have been scanned in official ballot mode, an election manager can only unconfigure the machine after scanned ballot data has been backed up. System administrators can unconfigure the machine at any time.

### Lifetime Scan Count

VxCentralScan maintains a lifetime scan count that gives the number of ballot sheets accepted throughout the scanner's lifetime. The count does not reset when the scanner is re-configured or when the software is updated. Other details of the lifetime scan count:

* The count does not include rejected and removed ballots e.g. unreadable ballots or ballots removed for manual adjudication
* If a batch is scanned but discarded rather than saved, those scans will still contribute toward the lifetime scan count
* The count includes ballots scanned in both official and test mode

## Batch Scanning

### Scanner Management

VxCentralScan is compatible with the Ricoh fi-8170, fi-7600, and fi-8950 production scanners. Once a scanner is detected, the user may begin scanning batches. The scanners are controlled via commands provided by the Debian `sane` package ("Scanner Access Now Easy") which creates a uniform API for most commercial scanners. As a result, no scanner-specific drivers are required.

### Batch Management

When the user triggers a batch scan, the scanner will start a batch and begin scanning sheets one at a time. The scanner pulls each sheet through and transfers a scanned image to the application which will then [interpret the ballot](ballot-interpretation.md) according to the current election definition. Scanning continues until the hopper is empty, at which point the user will choose to either continue the batch, save the batch, or discard the batch. The option to "continue the batch" would typically be used if the batch is too large for the hopper and needs to be loaded in parts. If the interpreter hits a ballot issue or adjudication reason, enumerated below, the user will choose between continuing the batch or discarding the batch.

The start time, end time, size, and index of all batches is tracked and displayed on the batch history page. If a mistake was made in organizing batches or adjudicating a ballot, election managers can delete any individual batch or delete all batches.

{% hint style="info" %}
**User Manual Reference:** [Central Scanning #Scan Ballot Batches](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxcentralscan/scanning-ballots#scan-ballot-batches "mention")
{% endhint %}

#### Batch UUIDs

The v4 UUID (universally unique identifier) for each batch is generated when the batch is first created. It is generated with the node package `uuid` which uses the system's underlying FIPS-compliant OpenSSL implementation to generate random bytes.

### Imprinting

All of the Ricoh scanners can be used with an optional imprinter:

* The fi-8170 attaches to the fi-819PRB imprinter
* The fi-7600 attaches to the fi-760PRB imprinter
* The fi-8950 has the fi-890PRB installed into it

As the ballot exits the scanner, the imprinter prints an identifier on the side margin of the ballot. The identifier is the batch's truncated UUID followed by the index of the sheet within the batch e.g. `378f6a69-3a5d90083e21_0000` for the first sheet in a batch. The identifier will appear in the CVR as the `BallotAuditId` with the full batch ID, e.g. `378f6a69-ad3f-25f2-234f-3a5d90083e21_0000`. Imprinting allows later reconciling CVRs to ballots such as in ballot comparison audits.

Imprinting is enabled by default but can be disabled by an election manager. Imprinting only occurs when an imprinter is detected and imprinting is also enabled.

## Ballot Issues & Adjudication

Batch scanning pauses whenever a ballot is not counted for any reason. Sometimes the ballot was not interpreted or cannot be accepted, in which case the ballot must be removed:

* **Vertical Streaks Detected** - the scanner may require cleaning
* **Unreadable** - the ballot image could not be successfully interpreted, possibly because it is not a valid ballot or because the image skew was too great
* **Wrong Ballot Mode** - test ballots in official ballot mode or official ballots in test ballot mode
* **Wrong Election** - the hash on the ballot does not match the currently configured election
* **Wrong Precinct** - if VxCentralScan is configured for a particular polling place and the ballot is not a part of that polling place

In other cases, the ballot requires adjudication. The adjudication reasons for VxCentralScan are set in the [system settings](election-package/#system-settings) as `centralScanAdjudicationReasons` and map to the following:

* **Overvote** - at least one contest is overvoted
* **Undervote** - at least one contest is undervoted
* **Marginal Mark** - at least one contest contains one or more marginal marks
* **Blank** - all contests are blank

In these cases, the affected contests will be highlighted on screen to the election manager and they will have the option to remove or tabulate the ballot.

{% hint style="info" %}
**User Manual Reference:** [adjudicate-ballots](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxcentralscan/scanning-ballots#adjudicate-ballots "mention")
{% endhint %}

## Exporting CVRs

CVRs must be exported onto a USB drive and taken to VxAdmin for aggregation and reporting. After ballots are interpreted, their images are saved to disk and their interpretation is stored in VxCentralScan's data store. On export, all CVRs are pulled from the data store, converted to the CVR CDF, and written to the USB drive.

{% hint style="info" %}
**User Manual Reference**: [saving-cast-vote-records-cvrs](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxcentralscan/scanning-ballots#saving-cast-vote-records-cvrs "mention")
{% endhint %}
