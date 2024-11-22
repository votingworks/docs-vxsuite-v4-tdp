# Preserving Voter Privacy

There is a tension between the requirement that (a) voter privacy should be strongly protected, and (b) Cast Vote Records should be continuously exported in order to ensure that they can be immediately available in the case of hardware failure. For example, if each scanned ballot naively results in the creation of a new CVR file on the USB stick with a timestamp, the order of CVRs is obviously preserved on the USB stick, as the file creation and modification timestamps reveal the order in which those CVRs were stored.

To meet both requirements, VxScan performs some amount of "shuffling" every time a CVR is saved to the USB drive. Every time a ballot is cast and its CVR is saved to the disk, VxScan picks one or two CVRs already stored on the USB drive, and updates their creation and modification time on the USB drive. This is the digital equivalent of taking one or two random ballots from a pile, and bringing them to the top of the pile. Thus, if an attacker were to view the CVRs on the USB drive, they would not be able to determine the order in which those ballots were cast, because of this constant shuffling.

The exact procedure used by VxScan, rather than just a `mv` operation, is three steps. This is done to ensure that all metadata for a given CVR is updated, including file creation time. Recall from [Broken link](broken-reference "mention") that a single CVR is structured, on disk, as a directory that contains the JSON data of the CVR and the ballot images for that CVR. Thus, the operations VxScan performs to move a single CVR "up to the top of the pile" is made up of three parts:

* first, rename the directory corresponding to the CVR to a new name that indicates it is being copied, specifically by appending -old:

`mv 4d6a9dad-e6d6-4a29-89bc-9ab915012b73/ 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-old/`

* then, copy this renamed directory back to the original name:

`cp -r 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-old/ 4d6a9dad-e6d6-4a29-89bc-9ab915012b73/`

* finally, delete the -old directory:

`rm -r 4d6a9dad-e6d6-4a29-89bc-9ab915012b73-old/`

This three-step operation ensures that

* all metadata for that CVR is updated, leaving no trace as to when that CVR was first saved to disk
* if a failure occurs at any point, it is possible to recover completely without losing any data.
