# Ballot QR Code Data Format

Both hand-marked paper ballots and machine-marked ballots contain QR codes. For hand-marked paper ballots, the QR code contains only metadata about the ballot. For machine-marked ballots, the QR code contains both metadata and voter choices.

In order to make the information as compact as possible, information is coded as binary values that reference the election definition. For example, instead of encoding the precinct name (e.g. "Fire Station Precinct") the QR code contains the index of the precinct within the [election definition](../system-overview/election-package/vxsuite-election-definition.md). If the precinct were the first precinct listed in the election definition, the value would be 0. If it were the second precinct listed in the election definition, the value would be 1. The binary sequence is ultimately encoded into the QR code as Base64 for broad compatibility with devices that scan QR codes.

## Decoding QR Codes Manually

Take following steps to decode a barcode manually and, in the case of a machine-marked ballot, manually verify the encoded selections are correct:

1. Scan the QR code with a smartphone camera or barcode reader. If your smartphone does not automatically detect a value, you may use any freely available QR code scanning app.
2. Copy and paste the scanned value into any Base64 to binary converter.
3. Inspect the binary values and compare them to the encodings described below. In order to make sense of the values, you will need the associated [election definition](../system-overview/election-package/vxsuite-election-definition.md) available for comparison.

You may use this process to verify that the encoded information in the ballot QR code matches the information presented on the ballot to human readers.

An easier, recommended approach is to simply scan the ballot(s) at VxScan or VxCentralScan. You can confirm the interpretation (and therefore in most cases, the QR code) is correct by looking at a results report. You can also inspect the [cast-vote-records.md](../system-overview/cast-vote-records.md "mention") exported from the scanner, which contain the images and interpretation for each ballot, to confirm that the metadata and voter selections were encoded and decoded correctly, similar to an [Image Audit](../system-security-auditing-and-logging/audit-procedure/#image-audits).

## HMPB QR Code Data Format

<table><thead><tr><th width="163.28125">Component</th><th>Length</th><th>Description</th></tr></thead><tbody><tr><td>HMPB Prelude</td><td>24 bits</td><td>The characters "VP2," which in binary appear as: <code>01010110 01010000 00110010</code></td></tr><tr><td>Ballot Hash</td><td>80 bits</td><td>See <a href="https://docs.voting.works/vxsuite-tdp-v4/system-overview/election-package#ballot-hash-and-election-package-hash">ballot hash documentation</a>. The 80 bits represent 20 4-bit hexadecimal characters.</td></tr><tr><td>Ballot Config</td><td>Variable</td><td>See <a data-mention href="ballot-qr-code-data-format.md#ballot-config-encoding">#ballot-config-encoding</a>.</td></tr><tr><td>Padding</td><td>0 - 7 bits</td><td>To ensure that the value in the QR code is composed of whole bytes, 0 bits are added until the data ends in a whole byte.</td></tr></tbody></table>

## Ballot Config Encoding

<table><thead><tr><th width="194.3125">Component</th><th width="175.78515625">Length</th><th>Description</th></tr></thead><tbody><tr><td>Precinct Index</td><td>13 bits</td><td>The index of the ballot's precinct in the election definition's list of precincts.</td></tr><tr><td>Ballot Style Index</td><td>13 bits</td><td>The index of the ballot's ballot style in the election definition's list of ballot styles.</td></tr><tr><td>Page Number</td><td>5 bits</td><td><strong>HMPB only</strong>. Encodes the page number of the ballot, one-indexed.</td></tr><tr><td>Test Ballot?</td><td>1 bit</td><td>When true, indicates a test ballot. When false, indicates an official ballot.</td></tr><tr><td>Ballot Type</td><td>4 bits</td><td>Indicates the ballot type - absentee ballots are <code>0001</code> and precinct ballots are <code>0000</code></td></tr><tr><td>Ballot ID Set?</td><td>1 bit</td><td>When true, indicates that the encoded ballot has an assigned ID that follows this bit. When false, indicates there is no ID.</td></tr><tr><td>Ballot ID</td><td>Variable, max 256 bytes</td><td><strong>Optional, HMPB only.</strong> Identifier for the ballot, UTF-8 encoding.</td></tr></tbody></table>

## BMD QR Code Data Format

Unlike the HMPB QR code, the BMD QR code actually encodes votes.

<table><thead><tr><th width="163.28125">Component</th><th width="177.578125">Length</th><th>Description</th></tr></thead><tbody><tr><td>BMD Prelude</td><td>24 bits</td><td>The characters "VX2," which in binary appear as: <code>01010110 01011000 00000010</code></td></tr><tr><td>Ballot Hash</td><td>80 bits</td><td>See <a href="https://docs.voting.works/vxsuite-tdp-v4/system-overview/election-package#ballot-hash-and-election-package-hash">ballot hash documentation</a>. The election's ballot hash is visible on most authenticated screens on all apps. The 80 bits represent 20 4-bit hexadecimal characters.</td></tr><tr><td>Ballot Config</td><td>Variable</td><td>See <a data-mention href="ballot-qr-code-data-format.md#ballot-config-encoding">#ballot-config-encoding</a>.</td></tr><tr><td>Vote "Roll Call"</td><td>Variable, 1 bit per contest in the election definition</td><td>Each bit corresponds to one contest and indicates whether the voter made any selections. For example, with four contests, <code>1010</code> would indicate votes in the first and third contests but not the second and fourth.</td></tr><tr><td>Vote Data</td><td>Variable</td><td>In sequence, all the vote data for the contests indicated in the "roll call."<br><br>For yes-no contests, a set bit <code>1</code>  indicates the "yes option" whereas an unset bit <code>0</code>  indicates the "no option."<br><br>For candidate contests, includes a bit for each candidate in the contest definition in the order of the contest definition. <code>1</code> is a vote and <code>0</code> is a non-vote. If the contest allows write-ins (meaning <code>allowWriteIns</code> is true in the election definition), there will be additional data here, described below. </td></tr><tr><td>Padding</td><td>0 - 7 bits</td><td>To ensure that the value in the QR code is composed of whole bytes, 0 bits are added until the data ends in a whole byte.</td></tr></tbody></table>

#### Write-In Encoding

If the contest does not allow write-ins (`allowWriteIns = false`) then the candidate contest data ends after the bits for the list of candidates. If the contest does allow write-ins (`allowWriteIns = true`), then write-in data will follow the candidate roll call and start with the number of write-ins. The maximum number of write-ins is the difference between the number of possible votes in the contest (e.g. is it a vote for one or vote for three contest) and the number of votes used on non-write-in candidates. The number of write-ins is written with the number of bits that would be required to write the maximum number of write-ins. For example, if a contest is "Vote for Five" and the ballot already contains two votes, the maximum number of votes is three. Three takes 2 bits to represent, so the number of write-ins will be `11`, `10`,  `01` , or `00` for 3, 2, 1, or 0 respectively.

After the number of write-ins, the write-ins are written in series, with 6 bits containing the length of the write-in, in bytes, and then the write-in itself in however many bytes after that. The bytes are in UTF-8 format.

## QR Code Specifications

HMPB and BMD QR codes are [Model 2 QR codes](https://www.qrcode.com/en/codes/model12.html) with [Level H error correction](https://www.qrcode.com/en/about/error_correction.html).

## Source Code

The source code and further technical documentation of how ballot QR codes are encoded and decoded can be found in the [ballot-encoder library](https://github.com/votingworks/vxsuite/tree/v4.0.1-release-branch/libs/ballot-encoder).
