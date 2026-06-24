# System Settings

The system settings file contains settings which are not specific to an election definition but do impact machine behavior.

## Authentication Settings

* `arePollWorkerCardPinsEnabled` - When set to `true`, poll worker cards are created with PINs which are then required when authenticating.
* `inactiveSessionTimeLimitMinutes` - Sets the number of minutes after which machines automatically lock due to inactivity.
* `numIncorrectPinAttemptsAllowedBeforeCardLockout` - Sets the number of times that a PIN can be entered incorrectly before the user has to wait extra time to retry.
* `overallSessionTimeLimitHours` - Sets the maximum number of hours for any session, regardless of activity.
* `startingCardLockoutDurationSeconds` - Sets the number of seconds that the user is locked out from retrying a PIN after the number of failed attempts specified by `numIncorrectPinAttemptsAllowedBeforeCardLockout`. Each subsequent failed attempt triggers a lockout double the length of the previous lockout.

## Scanning Thresholds

* `definite` - Specifies the percentage of a bubble that needs to be filled in for the system to interpret it as a vote.
* `marginal` - Specifies the percentage of a bubble that needs to be filled for the system to interpret it as a marginal mark that may need adjudication.
* `writeInTextArea` - Specifies the percentage of the write-in area that needs to be filled in for the tabulators to consider it a write-in. This is only relevant for jurisdictions that allow unmarked write-ins i.e. write-ins without an accompanying mark.

## Adjudication Settings

* `precinctScanAdjudicationReasons` - Specifies the reasons that a ballot scanned at VxScan should be flagged for adjudication. Supported reasons are overvotes, undervotes, blank ballots, or unmarked write-ins.
* `centralScanAdjudicationReasons` - Specifies the reasons that a ballot scanned at VxCentralScan should be flagged for adjudication. Supported reasons are overvotes, undervotes, blank ballots, or unmarked write-ins.
* `adminAdjudicationReasons` - Specifies the reasons for a ballot to appear in the VxAdmin adjudication queue in addition to write-ins. Supported reasons are undervotes, overvotes, marginal marks, and blank ballots.
* `areWriteInCandidatesQualified` - When set to `true`, write-ins can only be adjudicated for qualified write-ins added by an election manager. When set to `false`, adjudicators can add any unofficial write-in candidate on an ad hoc basis.

## Scanning Settings

* `disallowCastingOvervotes` - When set to `true`, scanners will always reject overvoted ballots. When set to `false`, VxScan will allow a voter to choose whether to reject or cast an overvoted ballot, and VxCentralScan will allow an election manager to choose whether to reject or tabulate an overvoted ballot.
* `allowOfficialBallotsInTestMode` - When set to `true`, official ballots will not be rejected in test mode. The setting is for jurisdictions where testing must take place on official ballots.
* `disableVerticalStreakDetection` - Disables the warning when streaks are detected when scanning ballots (which indicates that the scanner needs to be cleaned). Used as a failsafe in case of erroneous warnings.

## Other Settings

* `precinctScanEnableShoeshineMode` - When set to `true`, VxScan will run in "shoeshine mode," which will scan the same ballot repeatedly. Instead of ejecting the ballot after scanning it, VxScan will move it back to the input tray and scan it again. This mode is used only for internal testing and certification testing.
* `castVoteRecordsIncludeRedundantMetadata` - When set to `true`, scanners will include election and system metadata in each ballot's CVR as specified in the CVR CDF, rather than just including it once for the entire export. This extra information increases the size of the CVR export, degrading performance.
* `precinctScanEnableBallotAuditIds` - Enables the VxScan feature to read ballot IDs from hand marked paper ballot QR codes, encrypt them, and export them to cast vote records (to be used for post-election auditing).
* `precinctScanEnableWriteInImageReport` - Enables printing write-in image reports at VxScan after polls are closed.
* `precinctScanNumberOfReportCopies` - The number of polls reports that will be automatically printed at VxScan on polls transitions. When not set, VxScan will default to one. Used to streamline the poll worker flow in jurisdictions where multiple copies are always required.
* `bmdPrintMode` - Determines what type of ballots are printed at VxMark. Possible values:
  * `bubble_ballot` - Prints fully marked bubbled ballots onto blank paper.
  * `marks_on_preprinted_ballot` - Prints only marks onto pre-printed ballots.
  * `summary` - Prints summary ballots. Default value.
* `enableEarlyVoting` - Enables early voting features on VxScan and VxAdmin, e.g., setting a ballot casting mode of "Early Voting" on VxScan and tabulating early voting results separately on VxAdmin.
* Polls Close Time Settings
  * `electionDayPollsCloseTime` - Time value. Indicates when polls close on election day. Before the polls close time, the default poll worker screen will be the full poll worker menu. After the polls close time, the default poll worker screen will be the guided "Close Polls" flow. The time is a time only, rather than a timestamp, and is always interpreted in local time.
  * `disallowClosingPollsBeforeElectionDayPollsCloseTime` - If used in combination with `electionDayPollsCloseTime`, will fully disable the "Close Polls" option until the `electionDayPollsCloseTime`.
  * `disallowVxAdminTabulationBeforeElectionDayPollsCloseTime` - If used in combination with `electionDayPollsCloseTime`, will disable tabulation (i.e. generating reports) until the `electionDayPollsCloseTime`.
