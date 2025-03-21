# Procedural and Operational Security

VxSuite can be operated securely using the following these procedures. Some of these procedures are intentionally redundant for defense-in-depth as it is always expected that some operational mistakes are made.

## Using Proper Equipment

VxSuite should be used only with sanctioned equipment and peripherals. In particular, when connecting USB devices to any VxSuite component, use only USB devices of the type specified in this documentation, and only devices of known and reputable source.

## In Between Elections

When there are no active elections happening, VxSuite equipment should be physically secured so it is difficult to access and so that any access is evident at a later date.

* VxAdmin laptop and peripherals should be kept in their case, with numbered seals through both case seal points, preventing the case from being opened without breaking one or both seals.
* VxCentralScan laptop and peripherals should be kept in their case, with numbered seals through both case seal points, preventing the case from being opened without breaking one or both seals.
* The small Fujitsu/Ricoh scanner that works with VxCentralScan should be kept in its supplied soft case, with a numbered seal through the appropriate zipper hole, preventing the case from being opened without breaking the seal.
* The larger Fujitsu/Ricoh scanner that works with VxCentralScan should be kept in its supplied manufacturer box, with tamper evident tape along all sides and a numbered sticker seal on the main opening.
* VxScan should be kept closed with a numbered seal through one of the two seal points, preventing the case from being opened without breaking the seal.
* VxAdmin, VxCentralScan, VxScan, and the Fujitsu/Ricoh scanner, once sealed, should be kept in a safely locked room or storage area that only authorized election administrators have access to.
* The system admin smart cards should be kept in a safe or locked drawer, separately from VxAdmin. The PIN for the system admin smart card, if recorded on paper, should also be kept locked separate from both VxAdmin and the card.

You may consider occasionally resetting the PIN on the system administrator cards. This can be done using the VxAdmin laptop.

## During L\&A Testing

Both VxAdmin and VxScan are required for Logic & Accuracy testing. VxCentralScan is required if it is planned to be used for counting absentee ballots. VotingWorks's recommended practices take into account that this testing is often performed in view of the public.

* When retrieving all components from their locked storage location, ensure that the seal numbers match the logs.
* Keep clear and strong custody of all smart cards.
* Use the system admin card only long enough to un-configure VxAdmin, VxScan, and VxCentralScan from the last election, and to program VxAdmin for the new election. Then return the system admin card to its secure storage.

At the end of L\&A testing, ensure that the VxScan is ready and secured for election day:

* the correct USB drive is inserted into one of the two USB slots.
* the system has been switched to official-ballot mode.
* the VxScan is powered down.
* the VxScan case is closed and sealed.

If using VxCentralScan, ensure that that:

* it is switched to live mode
* it is shut down and put away in its case
* the case is closed and sealed.

Store all L\&A'ed equipment, with recorded seal numbers, in a secure location until election day.

## During an Election

Ensure that seals on equipment are untouched and appropriately numbered since L\&A.

### Opening The Polls

After setting up VxScan on the ballot box and opening the polls, ensure that:

* the ballot box is locked and/or sealed
* the auxiliary ballot box is locked and/or sealed
* the VxScan is attached to the ballot box using the locking mechanism
* the poll-worker access door on the VxScan is sealed shut

All seal numbers should be recorded.

### During Vote Casting

A poll worker should observe VxScan from afar at all times, ensuring voters are not attempting to break any seals.

If a ballot jam requires opening the poll worker door or the ballot box door, record the corresponding seal number before breaking, and ensure resealing afterwards, recording the new seal number(s).

### Scanning Absentee Ballots

VxCentralScan is only meant to be accessed by authorized election administrators. However, it is safe to project the screen via overhead projector, as long as the smart card PIN is entered via the keyboard, and not via the mouse.

### Closing the Polls

Unsealing the poll worker door is required to extract the USB drive after polls are closed. Ensure the seal number matches the expected value. Once the polls are closed and the USB drive is removed, take care to secure the chain of custody of the USB drive. VxScan should be closed up and sealed.

## After an Election&#x20;

Pack up all components in their respective cases and apply seals. Record those seals.

Additionally, any auditing or review of audit logs should be completed immediately after exporting those logs from the VxScan or Central system to a USB. If there is a concern about a break in the administrative chain of custody, the user should re-export the logs to a USB from the machine and can compare the original export with the re-export to determine the logs have not been tampered with while on the USB. The logs maintained on the system are unalterable and should be pulled and reviewed in one process to ensure that chain of custody is maintained.&#x20;
