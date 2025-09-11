# Safety, Security, Privacy, and Continuity of Operation

The following article and linked related articles are intended to cover VVSG 2.0 3.1.2-A.4.&#x20;

## Safety

Per VVSG 2.0 8.1-K - Eliminating Hazards, devices associated with the voting system are certified in accordance with the requirements of UL 62368-1. See [#eliminating-hazards](../audio-visual-and-display-screen-settings.md#eliminating-hazards "mention").  VxSuite hardware is designed to eliminate hazards from shock, radiation, heat, and mechanical dangers when used and maintained in accordance with the [VxSuite User Manual - v4](https://app.gitbook.com/o/-MG9xpTX0GFiCyXHEhNe/s/JtZutzGTdCzsGITrdiph/ "mention").

## Security

The system's provisions for security are detailed in the [system-security-auditing-and-logging](../system-security-auditing-and-logging/ "mention") section.

## Privacy

The provisions for voter privacy on VxScan are described in [preserving-voter-privacy.md](../system-security-auditing-and-logging/system-security-architecture/artifact-authentication/preserving-voter-privacy.md "mention"). The provisions for voter privacy on VxMarkScan are described in [#voter-privacy](../system-overview/vxmark-function.md#voter-privacy "mention").&#x20;

## Continuity of Operation

### Error Recovery

The voting system is designed to recover from errors as gracefully as possible. Displayed error messages, as enumerated in the error message sections in the [VxSuite User Manual - v4](https://app.gitbook.com/o/-MG9xpTX0GFiCyXHEhNe/s/JtZutzGTdCzsGITrdiph/ "mention"), are written to guide users to address the error. If the user encounters a recoverable error, the error message will instruct them to how to properly continue operation. For example if a smart card is inserted backward, the message will prompt the user to insert it correctly. If the user encounters an unrecoverable software error, the error message will prompt the user to restart the machine. The vast majority of problematic software states are resolved by a restart. After restarting, operation can continue.

### Machine Replacement

If a machine is damaged to the point of being inoperable, a replacement machine of the same type can be used. For larger customers, VotingWorks recommends that customers buy and maintain their own backup machines. For smaller customers, VotingWorks can provide replacement machines. If a replacement takes place in the middle of an election, users can take the following steps to substitute equipment:

* **VxScan -** Switch to scanning on the replacement VxScan and, at the end of the election, aggregate the cast vote records from both the damaged and replacement VxScans.
* **VxMarkScan** - Voters should start new voting sessions on the replacement VxMarkScan.
* **VxCentralScan** - The document scanner can simply be swapped. If the laptop is damaged and cast vote records were never exported, the scanned ballots should be re-scanned with the replacement laptop.
* **VxAdmin** - If the laptop is damaged, the laptop should be reconfigured with the election package and any cast vote records should be reloaded from the various USB drives.

### Paper Processes

VxSuite is ultimately a paper-based voting system and in the case of multiple overlapping failures, a part or the whole of the election can be transitioned to run on paper. If VxScan is damaged, ballots can be deposited in a ballot box and scanned later on VxCentralScan. If VxCentralScan is damaged, ballots can be fed into VxScan. If all scanners are damaged, ballots can be hand-counted.
