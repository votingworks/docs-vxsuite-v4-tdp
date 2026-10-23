# VxAdmin Function

VxAdmin acts as the election setup hub at the beginning of the election and the results aggregation and reporting hub at the end of an election (and also at the end of testing).

## Configuration and Election Packages

Only a [system administrator ](user-roles.md#system-administrator-role)can authenticate onto an unconfigured VxAdmin and configure it with an election package from an external system. The election package must be loaded via a USB drive. The election package must be a valid `.zip` [election-package](election-package/ "mention"). If the election package zip file, election definition file, system settings file, or metadata file are not valid, VxAdmin will surface an error to the user.

Once VxAdmin is configured, system administrators and election managers can export signed election packages. The exported election package is the same as the imported election package but is accompanied by a digital signature, which ensures that the election package was validated by a certified VxAdmin. The election packages loaded into VxMarkScan, VxScan, and VxCentralScan _must be signed_ and unsigned election packages will be rejected.

{% hint style="info" %}
**User Manual References:** [Configure VxAdmin](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxadmin-system-setup/configure-vxadmin "mention") & [Save Election Package](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxadmin-system-setup/save-election-package "mention")
{% endhint %}

## Smart Card Management

Smart cards are used for two-factor authentication on all machines in the system. They can only be programmed at VxAdmin with system administrator privileges.

Programming, like authentication, takes place via the laptop's built-in USB card reader. Once a card is inserted, the application is able to detect the card and read and write data by issuing APDUs (application protocol data units) which are the standard form of communication between smart card readers and smart cards.

For extensive details on the authentication scheme, see the [access control documentation](../system-security-auditing-and-logging/system-security-architecture/access-control.md).

{% hint style="info" %}
**User Manual Reference:** [Smart Cards and User Roles](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxadmin-system-setup/programming-cards "mention")
{% endhint %}

## USB Formatting

VxSuite components require data USB drives to be formatted with a single FAT32 or exFAT partition. The majority of USB drives are sold pre-formatted as FAT32, but some come in other formats. If an improperly formatted USB drive is inserted into a VxSuite component, it will be treated as if there is no USB drive. On VxAdmin, a drive formatted with an ext4 partition is treated as a backup drive rather than a data drive; see [#backup-and-restore](vxadmin-function.md#backup-and-restore "mention").

VxAdmin includes a utility to format USB drives to be compatible with the system. The utility is available only to system administrators. It will rewrite the partition table on the drive to include a single partition with an exFAT formatted filesystem that takes up all available space on the drive. exFAT is used rather than FAT32 so that files larger than 4 GB, such as large election packages, can be saved. The reformatting clears the USB drive and is thus a destructive action. If a USB drive is already correctly formatted, the feature can be used to clear its data. VxAdmin applies a new label to the reformatted USB drive in the form of **VxUSB-00000**, where the 0's can be any random alphanumeric characters.

Improperly formatted USB drives can only be detected and reformatted if there is _some_ partition already existing, so a USB drive without any partitions cannot be reformatted using VxAdmin.

{% hint style="info" %}
**User Manual Reference:** [USB Formatting](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/vxadmin-system-setup/usb-formatting "mention")
{% endhint %}

## CVR Management

The core post-election (and pre-election testing) function of VxAdmin is loading, managing, and tallying [cast vote records ](cast-vote-records.md)(CVRs).

### Loading CVRs

CVRs must be loaded from a USB drive. CVRs are exported from VxScan or VxCentralScan and are accompanied by a digital signature. CVRs without a digital signature cannot be loaded. CVR exports with digital signatures that do not match the content of the CVR exports cannot be loaded in order to prevent tampering.

The CVRs from the scanners are saved to a specific directory structure on the USB drive, but exports can be loaded from anywhere on a USB drive's filesystem. When selecting an export manually, the export's `metadata.json` file must be selected by the user.

When loading a full CVR export, each CVR is loaded into VxAdmin's backend store as one `cvrs` record. The CVR record includes a data blob representing the votes as interpreted by the scanner, a data blob representing the mark scores for all bubbles on the ballot (if a hand-marked paper ballot), and a series of metadata fields: ballot style, voting method (absentee vs. precinct), batch, scanner, precinct, sheet number within a multi-sheet ballot, and flags for adjudication reasons such as overvotes, undervotes, write-ins, or fully blank ballots. The metadata fields are used later on for filtering or aggregating tallies or ballot counts into groups.

Each write-in on a CVR will map to a `write-ins` record, whether it is an unmarked write-in or a proper write-in. The ballot images are also each saved as database records. The write-in record links the write-in to its respective CVR, to the ballot images, and eventually to its adjudication result. The write-in adjudication interface essentially iterates through all `write-ins` records on a per contest basis.

If an error is found when loading any single CVR in a CVR export, the entire export is rejected and a message is surfaced to the user. CVRs can be rejected for a variety of reasons: authentication failed; a file is incorrectly formatted; a CVR is not for a currently valid election, precinct, ballot style, or contest; a CVR with an identical ID has been loaded with different data. In everyday use of the system, all of these errors are either rare or impossible because VxAdmin will not allow loading CVR files from elections with mismatched metadata.

VxAdmin allows loading CVR exports that have already been partially loaded. For example, imagine that VxCentralScan exports CVRs after scanning 5 ballots and then again after scanning 10 ballots. If we first load the 5 CVR export and then the 10 CVR export, the 10 CVR export will successfully load but will ignore the CVRs that have already been imported.

{% hint style="info" %}
**User Manual Reference:** [Tally Results](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/election-night-guides/tally-results "mention")
{% endhint %}

### Ballot Mode

VxAdmin is always in one of three ballot modes:

* Unlocked Ballot Mode - no CVRs have been loaded
* Test Ballot Mode - test CVRs have been loaded
* Official Ballot Mode - official CVRs have been loaded

On VxAdmin, the ballot mode is determined by the ballot mode of the imported CVRs. VxAdmin differs in that respect from VxMarkScan, VxScan, and VxCentralScan, where the ballot mode is set directly by the election manager.

Once VxAdmin is in test ballot mode, only test CVRs can be subsequently loaded. Similarly once VxAdmin is in official ballot mode, only official CVRs can be subsequently loaded.

### Removing CVRs

CVR imports can be removed by the user before results are marked as official. The user can delete individual CVR imports or can delete all CVRs imports at once. The CVR data in the database along with all its dependent data - write-ins, ballot images, and adjudications - are permanently and irrecoverably deleted from the data store. If results have been marked as official, the only way to remove CVR imports is by unconfiguring VxAdmin.

## Adjudication

The tally reports from VxScan do not reflect any post-voting adjudication. All write-ins are simply "Write-In", unmarked write-ins are undervotes, and marginal marks are also undervotes.

VxAdmin allows election managers to perform on-screen adjudication for blank ballots, write-ins, marginal marks, overvotes, and undervotes. By default, only ballots with write-ins appear in the adjudication queue. If `MarginalMark` , `Overvote`, `Undervote` , or `BlankBallot` is included in the system settings as part of the list of `adminAdjudicationReasons` , ballots with any of the specified features will also appear in the queue.

* A marginal mark is defined as any mark over a bubble which has a score of at least the `marginal` threshold defined in the system settings but less than the `definite` threshold defined in the system settings.
* A blank ballot is defined as any ballot where no bubbles crossed the `definite` mark threshold

The ballots are ordered in the queue by ballot style. For example, all "Precinct 1" ballots would be grouped together and all "Precinct 2" ballots would be grouped together instead of them being intermixed. Within each ballot style, blank ballots are grouped behind non-blank ballots and summary ballots are grouped behind bubble ballots.

The adjudicator is presented with a full view of the ballot and a list of all contests on the ballot. They may flip the ballot from front to back or vice versa. Contests with issues are highlighted in both the ballot view and in the contest list. The adjudicator selects a contest to zoom in and resolve issues. The user can adjudicate any contest option from marked to unmarked or vice versa. When presented with a marginal mark, the user can choose to leave it as an undervote or adjudicate it as marked. For write-ins, they may adjudicate the write-in for a particular write-in candidate - more information in the next section. As the user makes changes, captions are used to indicate differences between the original interpreted values and the new adjudicated values. Once the adjudicator has resolved all issues on a ballot, they may confirm their changes and move on to the next ballot. Until confirmed, adjudications are "unsaved" and do not affect tabulation.

### Write-In Candidates

VxAdmin handles write-in candidates differently depending on whether the jurisdiction requires that write-in candidates must be "qualified" for their votes to count.

#### Qualified Write-In Mode

If `areWriteInCandidatesQualified` is true, then adjudicators can only allocate write-ins to qualified candidates or mark write-ins as invalid. The election manager can add qualified candidates at VxAdmin on a per-contest basis. If no qualified candidates are added for a contest, the only option for that contest's write-ins will be "Invalid". All qualified write-ins appear on tally reports regardless of their vote totals.

#### Open Write-In Mode

If `areWriteInCandidatesQualified` is false, write-in candidates are added on an ad hoc basis. The adjudicator has the option to add a new unofficial write-in candidate or select any previously added unofficial write-in candidate. The adjudicator may also adjudicate the write-in as "Invalid" or, in jurisdictions that allow it, for an official candidate that is already on the ballot. In open write-in mode, unofficial write-ins only appear on tally reports if they have a winning vote total.

{% hint style="info" %}
**User Manual Reference:** [Adjudication](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/election-night-guides/adjudication "mention")
{% endhint %}

## Manual Tallies

VxAdmin offers a way to enter manual tallies that are then added to reports. When manual tallies are present in a results export, they are always displayed separately from scanned tallies so that users can easily recognize the impact of manual results and recognize any human errors. The only exception to this rule is the CDF election results export in which, due to the limitations of the CDF, the manual and scanned tallies are simply combined.

The ballot style, precinct, and voting method (absentee vs. precinct) must be specified before entering manual tallies. By associating manual tallies with these pieces of metadata, they can be filtered and grouped according to those dimensions when creating reports. Notably, manual tallies are not associated with a batch or a scanner like CVRs. When filtering on batch or scanner, manual tallies are excluded. When grouping by batch or scanner, manual tallies are treated as a single batch or scanner.

The manual tallies for each contest are validated according to a standard formula:

$$
\text{total ballots} * \text{votes allowed in contest} = \text{total votes} + \text{total undervotes} + \text{total overvotes}
$$

The same formula also applies to all results generated from scanned ballots. If a vote-for-three contest is overvoted, it is considered three overvotes. If the contest tallies entered by the user are incomplete or invalid, the user is presented with warning messages.

In most cases, the ballot count will be the same across all contests. In some jurisdictions it is possible for different contests to have different ballot counts if, for example, someone votes on a ballot without local contests. In these cases, the user can override the ballot count on an individual contest basis.

Unofficial write-in candidates can also be allocated votes in manual tallies and new unofficial write-in candidates can be added directly from the manual tallies interface.

{% hint style="info" %}
**User Manual Reference**: [Manual Tallies](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/election-night-guides/manual-tallies "mention")
{% endhint %}

## Tallying & Reports

### Vote Tallying

Vote tallying is a multi-step process which takes place on the VxAdmin backend:

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

Every tally is specified by a set of filters and groupings. The filter defines which CVRs are excluded and included. For example, a filter might limit the CVRs to the CVRs for a specific precinct. The group determines how tallies are subdivided by CVR metadata. For example, there may be a grouping on precinct which generates tallies for each precinct separately. Groups enable multiple related tallies to be efficiently generated at once.

Filters and groupings are specified by the user directly with the tally report builder or implicitly with built-in reports.

#### Group Determination

If there are no groupings specified, there is only one set of tallies. If the precinct grouping is specified, there will be tallies for each precinct. If multiple groupings are specified, the possible resulting groupings need to be calculated. For example, if the precinct and ballot style groupings are both specified, only some combinations are possible because not all ballot styles exist in all precincts. If filters are specified, they may rule out certain groupings. For example, if the precinct grouping is specified but only Precinct A and Precinct B are included by the filter, then the Precinct C grouping will be excluded.

If batch or scanner parameters are included, then VxAdmin will not attempt to compute the possible groupings because they may be too numerous. The potential groups will be created opportunistically during tallying.

The purpose of computing the groups when possible, rather than always creating groups opportunistically, is to know which zero tallies to expect. When we group by precinct, we'd like to generate empty results for Precinct A even if no ballots for Precinct A were cast.

**CVR Aggregation**

The CVRs are pulled from the data store one by one and their vote data is added into an ongoing tally of ballots, contest option votes, overvotes, and undervotes. If the tallies are being grouped, the CVR will be added into the group that matches its metadata e.g. a CVR from a Precinct A ballot will be added to the Precinct A group. If `countCentralScanBallotsOnlyAfterAdjudication` is enabled in the system settings, CVRs from VxCentralScan that still require adjudication are skipped.

At this step in the process, the data does not contain any of the adjudication details from write-in adjudication.

CVR aggregation is the most computationally expensive step in the vote tallying so the results are cached. The cache is reset anytime a CVR file is added or removed or anytime a vote is adjudicated through write-in adjudication.

**Write-In Adjudication Aggregation**

The write-in adjudication records are summarized from the data store and their adjudication statuses are added into an ongoing tally of write-ins for official candidates, write-ins for unofficial candidates, invalid write-ins, and unadjudicated write-ins. They are filtered and grouped according to the same parameters as the CVRs.

{% hint style="info" %}
The write-in adjudication report is simply the results of the write-in adjudication aggregation step, without filter or group, formatted into a PDF.
{% endhint %}

#### Write-In Adjudication Hydration

The vote tallies from the CVRs are then hydrated with the aggregated write-in adjudication tallies to create vote tallies that include the results of write-in adjudication. Before hydration, the tallies represent all write-ins as generic write-ins. The counts for generic write-ins are reconciled to counts for specific official and unofficial candidates.

#### Manual Tallies Aggregation

Manual tallies are already aggregated in the sense that each can represent more than one ballot. Since they are divided by ballot style, precinct, and voting method, however, they may need to be _merged_ to match the groupings (or lack thereof) of the scanned vote tallies.

#### Manual Tallies Hydration

Manual tallies are then combined with the scanned tallies in one of two ways. For most reports, the manual tallies are paired with the scanned tallies but are not immediately added together. Reports can then display the manual and scanned tallies separately in addition to showing the total tallies. For the CDF election results report, however, the manual tallies and scanned tallies are added together because there is not a clear way to represent the difference between them in the CDF.

#### **Reporting**

The final step is for the VxAdmin backend to format the vote tallies into one of [VxAdmin's Results Export Formats](vxadmin-results-exports/) and export the result onto a USB drive or, if it is a PDF document, print it.

If `electionDayPollsCloseTime` and `disallowVxAdminTabulationBeforeElectionDayPollsCloseTime` are both set, the application will prevent generating reports until after the polls close time. In test mode, the same restriction does not apply. The behavior must vary between official and test mode because testing happens before election day.

{% hint style="info" %}
**User Manual Reference:** [Reports](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/election-night-guides/reports "mention")
{% endhint %}

### Ballot Count Tallying

Ballot counts are tallied as part of the vote tallying flow described above, but there is a separate tallying path that _only_ calculates the ballot counts. It is used when generating ballot count reports and exports from VxAdmin. It follows the same steps as vote tallying, but is more efficient because it can use the underlying SQLite database to generate tallies rather than iterating through each CVR one-by-one.

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

#### Ballot Count Definition

When tallying ballot counts, VxAdmin is actually tallying sheet counts. In an election where all ballots are a single sheet, there is no distinction between ballot counts and sheet counts. In an election with multi-sheet ballots, there may be different numbers of different ballot sheets. VxAdmin tallies each sheet separately, which is displayed on tally reports and ballot count reports.

The **Ballot Count** is defined in VxSuite as simply the count of first sheets. For example, if there are 1,000 first sheets and 999 second sheets, the ballot count will appear in reports as 1,000.

## Official vs. Unofficial Results

Results on VxAdmin are considered unofficial until the election manager marks them as official. As long as results are unofficial, CVRs can be loaded, write-ins can be adjudicated, and manual tallies can be added and edited. All reports and result exports are labelled as "Unofficial."

Once the results are final and often only after a jurisdiction's specific certification process, the election manager can mark results as official. All reports and result exports will then be labelled as "Official." CVRs can no longer be loaded, write-ins can no longer be adjudicated, and manual tallies can no longer be altered.

There are two ways to exit official results mode without unconfiguring VxAdmin:

* The system administrator can revert election results back to unofficial, which leaves all election data intact but allows it to be altered again by an election manager
* The election manager may remove _all_ election data at once, which would require restarting aggregation and adjudication from scratch

## Backup and Restore

A VxAdmin in host mode can save a complete backup of its election data to a backup USB drive, and an unconfigured VxAdmin can be restored from that backup. Restoring is intended for recovering from a failed or replaced laptop: the restored machine holds the same election, cast vote records, ballot images, adjudications, and manual tallies as the machine that saved the backup.

### Backup Drives

VxAdmin distinguishes backup drives from data drives by their filesystem. A drive with a FAT32 or exFAT partition is a data drive, used for election packages, cast vote records, reports, and logs. A drive with an ext4 partition is a backup drive. Both may be connected at the same time, and VxAdmin tracks each separately, so a backup can be saved while a data drive remains inserted. The backup and restore flows only ever read from or write to the backup drive.

ext4 is required because replacing a previous backup relies on an atomic directory exchange that FAT filesystems do not support. VxAdmin's USB formatting utility produces data drives only; it does not format backup drives. Backup drives are prepared by VotingWorks. Drive specifications and capacity guidance are in the user manual's [Supply List](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/miscellaneous/supply-list#backup-drives "mention").

### Backup Contents

A backup is a directory on the backup drive at `vxadmin-backups/<election folder name>/`, where the election folder name is the same one used for election packages and cast vote records on data drives. It contains:

* `workspace/` - a copy of the election data: a snapshot of the election database, every ballot image referenced by that snapshot, and the election package for the current election.
* `manifest.json` - the backup manifest, which records the manifest format version, the VxAdmin software version, the machine ID, the creation time, the election's ID, title, date, jurisdiction, and state, the number of cast vote records, and the path, size, and SHA-256 hash of every file under `workspace/`.
* `manifest.json.vxsig` - the manifest's digital signature, produced with the machine's TPM key as described in [artifact-authentication](../system-security-auditing-and-logging/system-security-architecture/artifact-authentication/ "mention"). Only the manifest is signed; every other file in the backup is covered by its hash within the manifest, so signing the manifest authenticates the whole backup.

A backup drive holds at most one backup per election. Saving a new backup of the same election replaces the previous one. Backups of different elections coexist on the same drive.

### Saving a Backup

System administrators and election managers can save a backup from the Election screen while VxAdmin is configured. Before saving, VxAdmin shows the details of the last backup of the current election already on the drive, if any. The machine can be locked while a backup is in progress and the backup continues in the background.

The backup proceeds in three phases shown to the user as preparing, saving files, and finishing:

1. **Preparing.** VxAdmin confirms it is in host mode and configured, that the backup drive is mounted and supports the final exchange, and that the internal disk has room for a database snapshot. It then snapshots the database using SQLite's online backup API, which produces a consistent copy without blocking the running application. The ballot images and election package to include are enumerated from the snapshot rather than the live database, so a change made during the backup cannot leave the backup internally inconsistent. These files are staged with hard links, so staging consumes no additional disk space beyond the snapshot. Finally, VxAdmin checks that the backup drive has room for the staged files.
2. **Saving files.** Each staged file is streamed to an in-progress directory on the backup drive, hashed as it is written, and recorded in the manifest. The manifest and its signature are written last.
3. **Finishing.** The in-progress directory is flushed to the drive, then exchanged atomically with the previous backup of the same election, if one exists, and the drive is flushed again. The previous backup is therefore replaced only once the new one is complete and on disk, and the drive never holds a partially written backup in the backup's place.

The user can cancel a backup during the first two phases. A canceled or failed backup's in-progress directory is discarded and the previous backup is left untouched.

### Restore Mode

Restoring replaces the entire contents of VxAdmin's workspace, so it is not performed by the running application. Instead, VxAdmin restarts into restore mode, a reduced version of the application that serves no election data and offers only the restore. A system administrator starts the process from the unconfigured Election screen by selecting "Restore from Backup", which schedules restore mode for the next boot and restarts the machine. Restore mode can only be entered from an unconfigured host-mode VxAdmin.

In restore mode, every screen carries a Restore Mode banner with a button to exit by restarting normally. Because the machine is unconfigured, only system administrators can unlock it. Once unlocked, VxAdmin prompts for a backup drive and lists every backup on it, showing each backup's election, jurisdiction, state, cast vote record count, and the machine and time that created it. Backups that cannot be read are listed separately.

### Restoring a Backup

After the user selects a backup and confirms, the restore proceeds in three phases shown as preparing, restoring files, and finishing:

1. **Preparing.** VxAdmin verifies the manifest's signature and reads the manifest from a private copy taken during verification, so the bytes it acts on are the bytes whose signature was checked. It then checks that the manifest version and software version match this machine's software, and that the signing machine's jurisdiction, taken from its certificate, matches this machine's jurisdiction. A backup signed by a different VxAdmin in the same jurisdiction is accepted and logged, since moving a backup between machines is how failed hardware is replaced. A backup from another jurisdiction is refused. VxAdmin then confirms the workspace is unconfigured, confirms the internal disk has room for the backup, empties the workspace, and marks a restore as in progress.
2. **Restoring files.** Each file listed in the manifest is copied from the backup drive into the workspace and verified against its size and hash as it lands. A file that does not match fails the restore.
3. **Finishing.** VxAdmin opens the restored database to confirm it holds the election the manifest promised, flushes the restored files to disk, and clears the in-progress marker.

The user can cancel during the first two phases. A canceled or failed restore empties the workspace, so VxAdmin is left either fully restored or unconfigured, never in between. If a restore is interrupted by a power loss, the in-progress marker causes the next boot to discard what was left behind, log the interruption, and start unconfigured. On completion the user is prompted to restart; VxAdmin then starts normally, configured with the restored election.

Because a backup drive is removable media outside VxAdmin's control, the restore treats its contents as untrusted. Every file is read at most once and only up to the size the manifest promises, and nothing is parsed from the drive until its signature or hash has been checked.

## Networking & Multi-Station Adjudication

In order to adjudicate high volumes of ballots, additional adjudication station VxAdmins can be networked to a host VxAdmin. The adjudication station VxAdmins are only permitted to adjudicate ballots and to do basic system workflows such as exporting logs, adjusting the date and time, and performing signed hash validation. Any VxAdmin can be switched between "Host Mode" and "Adjudication Station Mode".

The host VxAdmin is connected to the adjudication stations via an ethernet network switch. In order for the network to be valid, all VxAdmins must have the same software version and there must be only one host VxAdmin. There is zero configuration required other than connecting components via ethernet cables.

The host VxAdmin is able to toggle multi-station adjudication on or off. Adjudication stations may only begin adjudication after it is enabled by the host VxAdmin.

The adjudication stations do not need to be configured individually - they pull their configuration from the host while connected.

Unlike the host VxAdmin, which can navigate forward and backward through the entire queue of ballots needing adjudication, the adjudication stations are simply assigned the next ballot in the queue. After that ballot is adjudicated, the next ballot is assigned. Whenever a ballot is being adjudicated by the host or any adjudication station, it cannot be assigned to another adjudication station and cannot be adjudicated by the host.

An adjudication station cannot skip a ballot. Instead, it can escalate the ballot to the host for election manager review, which discards any unsaved changes, releases the station's claim, and assigns the station the next ballot in the queue. Escalated ballots are flagged on the host, which can work through them as a separate queue or encounter them in the main queue, where they remain in their original position. The host cannot escalate ballots and resolves an escalated ballot by adjudicating it.

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption><p>VxAdmin Network Diagram</p></figcaption></figure>

#### Network Implementation

The networking implementation is a zero-configuration, host-advertised, client-pull model. There is no central registry or manual IP entry; everything is built on mDNS discovery and short-interval polling. The host advertises itself on the local network using `avahi`. When a VxAdmin starts in host mode, it publishes a network service named for its machine ID on its peer port. Adjudication stations discover hosts by browsing to find one and only one host-advertised service, and refuse to proceed if they detect more than one. Once a station finds the host, all communication flows over a dedicated host-to-station API, separate from the API the host's own UI uses: stations register themselves, pull down the election configuration, claim and release ballots from the queue, and submit completed adjudications, all by calling the host — the host never pushes to the stations. Each station runs this exchange on a short polling loop (every couple of seconds), which doubles as a heartbeat: on each cycle it confirms the host is still reachable, learns whether the host currently has multi-station adjudication enabled, and re-syncs the election configuration if it has changed since the last cycle. A station that stops polling simply ages out, at which point the host releases any ballots it was holding so they can be reassigned.

For more details on how networking is set up at the operating system level, see [networking.md](../system-security-auditing-and-logging/system-security-architecture/networking.md "mention").

## Printer Management

VxAdmin prints reports via an attached printer. The supported printer is the HP LaserJet Pro 4001dn. All reports are also available as PDFs so, in the event of a printer failure, reports will still be available.

VxAdmin interfaces with the printer through CUPS, the open-source printing system developed by Apple and installed on our Debian system. When a printer is attached, it is registered with the CUPS server and made available to the application. VxAdmin is able to send print jobs to the printer via CUPS commands. The HP LaserJet Pro does not require any additional third-party or in-house driver because it supports the IPP (Internet Printing Protocol) which CUPS then utilizes.

When a print job is submitted via CUPS, CUPS sends it to the printer using the IPP protocol. VxAdmin waits until CUPS reports it has successfully sent the entire job to the printer, at which point it logs success. If the printer is disconnected before CUPS can send the entire job, VxAdmin will log the failure. In these cases it's possible that the printer still prints an incomplete document or error code. Whenever the printer is disconnected, any pending jobs are cancelled to avoid unexpected prints on reconnection.

Note that VxAdmin can only connect with one printer at a time and will always connect with the first attached printer.
