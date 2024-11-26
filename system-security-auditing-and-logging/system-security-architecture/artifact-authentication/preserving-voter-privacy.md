# Preserving Voter Privacy

There is a tension between the requirement that (a) voter privacy should be strongly protected, and (b) cast vote records should be continuously exported in order to ensure that they can be immediately available in the case of hardware failure. For example, if each scanned ballot naively results in the creation of a new CVR file on the USB drive with a timestamp, the order of CVRs is obviously preserved on the USB drive, as the file creation and modification timestamps reveal the order in which those CVRs were stored.

To meet both requirements, VxScan performs some amount of "shuffling" every time a CVR is saved to the USB drive. Every time a ballot is cast and its CVR is saved to the disk, VxScan picks one or two CVRs already stored on the USB drive and updates their creation and modification time on the USB drive. This is the digital equivalent of taking one or two random ballots from a pile and bringing them to the top of the pile. Thus, if an attacker were to view the CVRs on the USB drive, they would not be able to determine the order in which those ballots were cast, because of this constant shuffling.

Recall from [cast-vote-records.md](../../../system-overview/cast-vote-records.md "mention") that a single CVR is structured, on disk, as a directory that contains the JSON data of the CVR and the ballot images for that CVR. The VxScan operation performed to move a single CVR "up to the top of the pile" involves four steps:

* Copy the CVR directory contents:

`cp -r 4d6a9dad-e6d6-4a29-89bc-9ab915012b73/ 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-temp/`

* Once copying completes, mark the new directory as complete:

`mv 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-temp/ 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-temp-complete/`

* Delete the old directory:

`rm -r 4d6a9dad-e6d6-4a29-89bc-9ab915012b73/`

* Rename the new directory:

`mv 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-temp-complete/ 4d6a9dad-e6d6-4a29-89bc-9ab915012b73/`

This four-step operation ensures that:

* All metadata for that CVR (parent directory and children files) is updated, leaving no trace as to when that CVR was first saved to disk.
* If a failure occurs at any point, it is possible to recover completely without losing any data.

## Code Links

Refer to the following codebase links for more detail on this operation:

* [https://github.com/votingworks/vxsuite/blob/main/libs/backend/src/cast\_vote\_records/file\_system\_utils.ts](https://github.com/votingworks/vxsuite/blob/main/libs/backend/src/cast_vote_records/file_system_utils.ts)
