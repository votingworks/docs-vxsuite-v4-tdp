# Procedural and Operational Security

VxSuite can be operated securely by following these procedures. Some of these procedures are intentionally redundant for defense-in-depth as it is always expected that some operational mistakes are made.

## Using Proper Equipment

VxSuite should be used only with sanctioned equipment and peripherals.

* do not connect USB devices of unknown source to any VxSuite component.
* do not connect any USB device to VxSuite ports other than those explicitly sanctioned in this documentation.

## In Between Elections

When there are no active elections happening, VxSuite equipment should be physically secured so it is difficult to access and so that any access is evident at a later date.

* VxAdmin laptop and peripherals should be kept in their case, with a numbered seal through the appropriate hole, preventing the case from being opened without breaking the seal.
* VxCentralScan laptop and peripherals should be kept in their case, with a numbered seal through the appropriate hole, preventing the case from being opened without breaking the seal.
* The Fujitsu scanner that works with VxCentralScan should be kept in its supplied soft case, with a numbered seal through the appropriate zipper hole, preventing the case from being opened without breaking the seal.
* VxScan should be kept closed with a numbered seal through the appropriate hole, preventing the case from being opened without breaking the seal.
* VxAdmin, VxCentralScan, VxScan, and the Fujitsu scanner, once sealed, should be kept in a safely locked room or storage area that only authorized election administrators have access to.
* The system admin smartcards should be kept in a safe or locked drawer, separately from VxAdmin. The PIN for the system admin smartcard, if recorded on paper, should also be kept locked separate from both VxAdmin and the card.

It is a good practice, every year or so, to reset the PIN on the system administrator cards. This can be done using the VxAdmin laptop.

## During L\&A Testing

Both VxAdmin and VxScan are required for Logic & Accuracy testing. VxCentralScan is required if it is planned to be used for counting absentee ballots. VotingWorks's recommended practices take into account that this testing is often performed in view of the public.

* When retrieving all components from their locked storage location, ensure that the seal numbers match the logs.
* Keep clear and strong custody of all smartcards.
* Use the system admin card only long enough to un-configure VxAdmin, VxScan, and VxCentralScan from the last election, and to program VxAdmin for the new election. Then return the system admin card to its secure storage.

At the end of L\&A testing, ensure that the VxScan is ready and secured for election day:

* the correct USB drive is inserted into one of the two USB slots.
* the system has been switched to live mode.
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
* the VxScan is sealed to the box
* the poll-worker access door on the VxScan is sealed shut

All seal numbers should be recorded.

### During Vote Casting

A poll worker should observe VxScan from afar at all times, ensuring voters are not attempting to break any seals.

If a ballot jam requires opening the poll worker door, record the seal number before opening, and ensure the poll worker door is resealed afterwards, recording the new seal number.

### Scanning Absentee Ballots

VxCentralScan is only meant to be accessed by authorized election administrators. However, it is safe to project the screen via overhead projector, as long as the smartcard PIN is entered via the keyboard, and not via the mouse.

### Closing the Polls

Unsealing the poll worker door is required to close the polls. Ensure the seal number matches the expected value. Once the polls are closed and the USB drive is removed, take care to secure the chain of custody of the USB drive. VxScan should be closed up and sealed.

## After an Election&#x20;

Pack up all components in their respective cases and apply seals. Record those seals.

Additionally, any auditing or review of audit logs should be completed immediately after exporting those logs from the VxScan or Central system to a USB. If there is a concern about a break in the administrative chain of custody, the user should re-export the logs to a USB from the machine and can compare the original export with the re-export to determine the logs have not been tampered with while on the USB. The logs maintained on the system are unalterable and should be pulled and reviewed in one process to ensure that chain of custody is maintained.&#x20;
