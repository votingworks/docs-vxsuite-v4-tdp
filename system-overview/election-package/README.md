# Election Package

The election package contains all of the information that defines an election. VxAdmin is configured by inserting a USB drive and selecting an election package from the drive.

After VxAdmin is configured, the election package can then be digitally signed and exported onto a USB drive in order to configure the other system components. The [digital signature](../../system-security-auditing-and-logging/system-security-architecture/artifact-authentication/) verifies that the election package is legitimate. The other devices require that the signature is present. As a result, an election package from outside the system cannot be used to directly configure VxScan, VxMark, VxMarkScan, VxCentralScan, or VxPrint.

## Election Package Contents

The election package is a zip archive (a `.zip` file). The zip archive has the following content:

* Election Definition (`election.json`)
* App Strings (`appStrings.json`)
* Audio IDs (`audioIds.json`)
* Audio Clips (`audioClips.jsonl`)
* Ballots (`ballots.jsonl`)
* Registered Voter Counts (`registeredVotersCounts.json`)
* System Settings (`systemSettings.json`)
* Metadata (`metadata.json`)

### Election Definition

The election definition file includes the information that defines the election and ballots, including but not limited to definitions for contests, ballot styles, precincts, polling places, parties, multi-lingual ballot translations, and ballot layouts. The system accepts two formats - the [VxSuite Election Definition](vxsuite-election-definition.md) format or the [Ballot Definition CDF](ballot-definition-cdf.md). When using the Ballot Definition CDF, some features are not available.

The election definition file is required to be present in the election package.

### App Strings

The app strings file contains all voter-facing strings in the user interface and their translations. For example, at the beginning of the voter flow in VxMark there is a button labelled, by default, "Start Voting." If the voter has set VxMark to another language, however, the button will display the translation for that language specified in the app strings file. Additionally, the default English text can be overridden by specifying a different English value in the app strings file.

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
* The language codes in the app strings file are [IETF language tags](https://www.w3.org/International/articles/language-tags/).
* The keys for the various user interface app strings (e.g. `buttonStartVoting`) are defined in VxSuite's [app strings catalog](https://github.com/votingworks/vxsuite/blob/v4.0.7/libs/ui/src/ui_strings/app_strings_catalog/latest.json).

The app strings file is optional. If not provided, default English strings will be used.

### Audio IDs & Audio Clips

The audio IDs file is a JSON file structured identically to the app strings file except that instead of containing text values for each voter string, it contains audio IDs for each voter string. Each audio ID corresponds to an entry in the audio clips file.

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

### Ballots

The ballots file contains pre-rendered ballot PDFs, one per unique combination of ballot style, precinct, ballot type (precinct or absentee), and ballot mode (official or test). It is a [JSONL](https://jsonlines.org/) file in which each line is a JSON object describing one ballot, with the PDF itself encoded in base 64. For example, a single line would appear as:

```json
{ "ballotStyleId": "1_en", "precinctId": "precinct-1", "ballotType": "precinct", "ballotMode": "official", "encodedBallot": "JVBERi0xLj..." }
```

These pre-rendered ballots allow VxMark and VxPrint to produce printed ballots without rendering them on the device.

The ballots file is optional. It is required when using VxPrint or when using VxMark configured to print full-faced ballots.

### Registered Voter Counts

The registered voter counts file records the number of registered voters in each precinct, or in each split for precincts that are divided into splits. A precinct without splits maps directly to a count, while a precinct with splits maps to a count per split:

```json
{
  "precinct-1": 1200,
  "precinct-2": {
    "splits": {
      "precinct-2-split-a": 450,
      "precinct-2-split-b": 375
    }
  }
}
```

VxAdmin uses these counts to produce voter turnout reports, which compare ballots cast against registered voters to calculate turnout. Counts must be provided for all precincts or not at all.

The registered voter counts file is optional. If it is not provided, voter turnout reports cannot be generated.

### System Settings

[system-settings.md](system-settings.md "mention")

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

## Ballot Rotation

Ballot rotation is specified by the defined candidate order in each ballot style as opposed to specifying a rule that the voting system should apply to a given list of candidates. The system supports tabulation of ballots with any type of candidate ordering. This enables flexibility for jurisdiction-specific ballot rotation rules that can be defined in the source system creating the ballot definition.

Election officials can verify their ballot rotation configuration by configuring VxMarkScan, selecting different precincts (and by extension ballot styles), and confirming that the order of candidates differs per precinct as expected.
