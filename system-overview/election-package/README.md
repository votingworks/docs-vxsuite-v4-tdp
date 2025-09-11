# Election Package

The election package contains all of the information that defines an election. VxAdmin is configured by inserting a USB drive and selecting an election package from the drive.

After VxAdmin is configured, the election package can then be digitally signed and exported onto a USB drive in order to configure VxScan, VxCentralScan, and VxMarkScan. The [digital signature](../../system-security-auditing-and-logging/system-security-architecture/artifact-authentication/) verifies that the election package is legitimate. The other devices require that the signature is present. As a result, an election package from outside the system cannot be used to directly configure VxScan, VxCentralScan, or VxMarkScan.

## Election Package Contents

The election package is a zip archive (a `.zip` file). The zip archive contains 6 files:

* Election Definition (`election.json`)
* App Strings (`appStrings.json`)
* Audio IDs (`audioIds.json`)
* Audio Clips (`audioClips.jsonl`)
* System Settings (`systemSettings.json`)
* Metadata (`metadata.json`)

### Election Definition

The election definition file includes the information that defines the election and ballots, including but not limited to definitions for contests, ballot styles, precincts, parties, multi-lingual ballot translations, and ballot layouts. The system accepts two formats - the [VxSuite Election Definition](vxsuite-election-definition.md) format or the [Ballot Definition CDF](ballot-definition-cdf.md). When using the Ballot Definition CDF, some features are not available.&#x20;

The election definition file is required to be present in the election package.

### App Strings

The app strings file contains all voter-facing strings in the user interface and their translations. For example, at the beginning of the voter flow in VxMarkScan there is a button labelled, by default, "Start Voting." If the voter has set VxMarkScan to another language, however, the button will display the translation for that language specified in the app strings file. Additionally, the default English text can be overridden by specifying a different English value in the app strings file.

In the case of specifying a Spanish translation and overriding the English translation for "Start Voting", which has an internal key of `buttonStartVoting`, the following values and overall structure would appear in the app strings file:

```json
{
  "en": {
    ...
    "buttonStartVoting": "Begin Voting",
    ...
  },
  "es-US": {
    ...
    "buttonStartVoting": "Empezar a votar",
    ...
  }
}
```

**Notes:**

* Voter-facing strings that appear on ballots (contest names, candidate names, the name of the jurisdiction, etc.) are not included in the app strings file because they are already included in the election definition.
* The language codes in the app strings file are the [IETF language tags](https://www.w3.org/International/articles/language-tags/) for supported VxSuite languages: English, Spanish, Simplified Chinese, and Traditional Chinese.
* The keys for the various user interface app strings (e.g. `buttonStartVoting`) are defined in VxSuite's [app strings catalog](https://github.com/votingworks/vxsuite/blob/v4.0.2/libs/ui/src/ui_strings/app_strings_catalog/latest.json).

The app strings file is optional. If not provided, default English strings will be used.

### Audio IDs & Audio Clips

The audio IDs file is a JSON file structured identically to the app strings file except that instead of containing text values for each voter string, it contains audio IDs for each voter string. Each audio ID corresponds to an entry in the audio clips file.&#x20;

```json
{
  "en": {
    ...
    "buttonStartVoting": "AUDIO_ID_1",
    ...
  },
  "es-US": {
    ...
    "buttonStartVoting": "AUDIO_ID_2",
    ...
  }
}
```

Each row of the audio clips file contains one audio clip with relevant metadata. The audio itself appears as an MP3 file encoded in base 64. For example, a row representing an audio clip for the "Start Voting" button would appear as:

```json
{ "languageCode": "en", "id": "AUDIO_ID_1", "dataBase64": "YnV0dG9uU3..." }
{ "languageCode": "es-US", "id": "AUDIO_ID_2", "dataBase64": "DnX0eG6uY3..." }
...
```

Together, the two files allow specifying audio playback for any text read to a voter in audio mode, including both non-English translations and English overrides.

The audio IDs and audio clips files are optional. If they are not provided, audio playback will be disabled.

### System Settings

The system settings file contains settings which are not specific to an election definition but do impact machine behavior.

* Authentication Settings
  * `arePollWorkerCardPinsEnabled` - When set to `true`, poll worker cards are created with PINs which are then required when authenticating.
  * `inactiveSessionTimeLimitMinutes`- Sets the number of minutes after which machines automatically lock due to inactivity.
  * `numIncorrectPinAttemptsAllowedBeforeCardLockout`- Sets the number of times that a PIN can be entered incorrectly before the user has to wait extra time to retry.
  * `overallSessionTimeLimitHours`- Sets the maximum number of hours for any session, regardless of activity.
  * `startingCardLockoutDurationSeconds` - Sets the number of seconds that the user is locked out from retrying a PIN after the number of failed attempts specified by  `numIncorrectPinAttemptsAllowedBeforeCardLockout`. Each subsequent failed attempt triggers a lockout double the length of the previous lockout.
* Scanning Thresholds
  * `definite` - Specifies the percentage of a bubble that needs to be filled in for the system to interpret it as a vote.
  * `marginal` - Specifies the percentage of a bubble that needs to be filled for the system to interpret it as a marginal mark that may need adjudication.
  * `writeInTextArea` - Specifies the percentage of the write-in area that needs to be filled in for the tabulators to consider it a write-in. This is only relevant for jurisdictions that allow unmarked write-ins i.e write-ins without an accompanying mark.
* Adjudication Reasons
  * `precinctScanAdjudicationReasons` - Specifies the reasons that a ballot scanned at VxScan should be flagged for adjudication. Supported reasons are overvotes, undervotes, blank ballots, or unmarked write-ins.&#x20;
  * `centralScanAdjudicationReasons` - Specifies the reasons that a ballot scanned at VxCentralScan should be flagged for adjudication. Supported reasons are overvotes, undervotes, blank ballots, or unmarked write-ins.&#x20;
  * `adminAdjudicationReasons` - Specifies the reasons for a ballot to appear in the VxAdmin adjudication queue in addition to write-ins. The only supported reason is marginal marks.
  * `disallowCastingOvervotes` - When set to `true`, scanners will always reject overvoted ballots. When set to `false`, VxScan will allow a voter to choose whether to reject or cast an overvoted ballot, and VxCentralScan will allow an election manager to choose whether to reject or tabulate an overvoted ballot.
  * `allowOfficialBallotsInTestMode` - When set to `true`, official ballots will not be rejected in test mode. The setting is for jurisdictions where testing must take place on official ballots.
* Other
  * `precinctScanEnableShoeshineMode` - When set to `true`, VxScan will run in "shoeshine mode," which will scan the same ballot repeatedly. Instead of ejecting the ballot after scanning it, VxScan will move it back to the input tray and scan it again. This mode is used only for internal testing and certification testing.
  * `castVoteRecordsIncludeRedundantMetadata` - When set to `true`, scanners will include election and system metadata in each ballot's CVR as specified in the CVR CDF, rather than just including it once for the entire export. This extra information increases the size of the CVR export, degrading performance.
  * `disableVerticalStreakDetection` - Disables the warning when streaks are detected when scanning ballots (which indicates that the scanner needs to be cleaned). Used as a failsafe in case of erroneous warnings.
  * `precinctScanEnableBallotAuditIds` - Enables the VxScan feature to read ballot IDs from hand marked paper ballot QR codes, encrypt them, and export them to cast vote records (to be used for post-election auditing).

The system settings file is optional. If not provided, the following default settings will be used:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "auth": {
    "arePollWorkerCardPinsEnabled": false,
    "inactiveSessionTimeLimitMinutes": 30,
    "numIncorrectPinAttemptsAllowedBeforeCardLockout": 5,
    "overallSessionTimeLimitHours": 12,
    "startingCardLockoutDurationSeconds": 15
  },
  "markThresholds": {
    "definite": 0.07,
    "marginal": 0.05,
    "writeInTextArea": 0.05
  },
  "centralScanAdjudicationReasons": [],
  "precinctScanAdjudicationReasons": [],
  "adminAdjudicationReasons": [],
  "disallowCastingOvervotes": false,
  "allowOfficialBallotsInTestMode": false,
  "precinctScanEnableShoeshineMode": false,
  "castVoteRecordsIncludeRedundantMetadata": false,
  "disableVerticalStreakDetection": false,
  "precinctScanEnableBallotAuditIds": false
}
</code></pre>

### Metadata

The metadata file is a JSON file that contains a single key, `version`. In the current software version, the value will only ever be `"latest"`. In other words, the metadata file is a JSON file with the contents:

```json
{
  "version": "latest"
}
```

In future software versions, the `"version"` value will be used to differentiate versions of the election package that correspond to different software versions. For example, if a user flow is updated, a new app string may be added and the `"version"` value will indicate which app strings to expect.

## Ballot Hash and Election Package Hash

There are two hashes for each election which are both critical to operation and security of each election.

The **ballot hash** is the SHA256 hash of the election definition file and represents a snapshot of all election-specific data which determines the ballot, including contest definitions and ballot layout. Ballots must include a machine-readable version of the ballot hash (e.g. a QR code or a pattern of timing marks). When a ballot is scanned, the scanner checks to make sure the ballot has the expected ballot hash. The ballot hash from the ballot must match the ballot hash from the scanner's configured election definition.

If any election content changes, the ballot hash will change, meaning the system will consider it to be a new election definition, and any ballots with a different ballot hash will not scan. The system's strict checking of the ballot hash prevents situations where a change to the election definition leads to ballots being miscounted (for example, if the order of two candidates is swapped). As a result, any changes to the election definition require reprinting all ballots.

The **election package hash** is the SHA256 hash of the entire election package, which includes both the election definition and all other files. The election package hash is displayed on screen to election managers and system administrators. It allows the user to ascertain which election package was used to configure a machine. The election package hash is _not_ used during ballot scanning.

For example, imagine that an election administrator wants to change the audio clip for candidate's name. The audio clip is not a part of the election definition but it is a part of the election package, so the ballot hash remains the same while the election package hash changes. The election administrator can reconfigure VxMarkScan with an updated election package but does not have to reprint ballots.

The **election ID** shown on screen and included in printed reports contains a shortened version of both the ballot hash and the election hash in the format: `{ballot hash}-{election hash}`. For example, with ballot hash `083e2e0afbb19191a4d2850562ddef050ff860b0d61acee15d3bb26954932941` and election hash `db5c379b71accbf991e42ab23d26202f88b2539b6c69b814a0d3c8dc9f4072dc`, the election ID would be: `083e2e0-db5c379`. This enables identification of both the specific election package and election definition that a machine is configured with.
