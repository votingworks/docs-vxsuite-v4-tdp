# Hashing of Continuously Exported Cast Vote Records

## Continuous Export

VxSuite precinct scanners export cast vote records (CVRs) to USB drive continuously, as ballots are cast. Continuous export also allows for a speedy polls close, as cast vote records need not be exported all at once on polls close.

## Merkle Tree Structure

To perform continuous export while also keeping signatures, i.e., authenticity information, up-to-date, the scanner must be able to write both CVRs and authenticity information incrementally. Hashing and signing only the new data is not sufficient; an up-to-date root hash and signature are required. A [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) structure accomplishes this efficiently.

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Assuming every CVR has a random universally unique identifier (UUID), e.g., 4d6a9dad-e6d6-4a29-89bc-9ab915012b73, the following structure can be used:

```
<cvr-directory-name>.vxsig ← Signature on root-hash.txt
<cvr-directory-name>/
  root-hash.txt ← hash( concatenation of all * hashes )
  4/
    4-hash.txt ← hash( concatenation of all 4* hashes )
    4d/
      4d-hash.txt ← hash( concatenation of all 4d****... hashes )
      4d6a9dad-e6d6-4a29-89bc-9ab915012b73/
        4d6a9dad-e6d6-4a29-89bc-9ab915012b73-hash.txt
        cast-vote-record-report.json
        Images
```

### On the Machine and on the USB Drive

The nested structure above describes the tree; it is not how files are laid out on the USB drive. The scanner keeps the tree's intermediate hashes on its internal disk and updates them as each cast vote record is added, so the root hash can be recomputed without reading anything back from the USB drive. Computing hashes only from the scanner's own records protects against [compromised or faulty USB drives](https://github.com/votingworks/vxsuite/pull/3554).

The USB drive holds a flat structure, one directory per cast vote record, and VxSuite signs a `metadata.json` file that carries the root hash along with other export metadata:

```
<cvr-directory-name>.vxsig ← Signature on metadata.json
<cvr-directory-name>/
  metadata.json
  4d6a9dad-e6d6-4a29-89bc-9ab915012b73/
    cast-vote-record-report.json
    Images
```

Sample `metadata.json`:

```
{
  "arePollsClosed": false,
  "castVoteRecordRootHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  ...
}
```

## Import

Whenever a machine imports a CVR directory, it authenticates the CVRs by 1) verifying the signature on the metadata.json file and 2) recomputing the “castVoteRecordRootHash” in metadata.json from scratch to confirm that it is correct.

## Code Links

Refer to the following code links for more details:

* [libs/auth/src/cast\_vote\_record\_hashes.ts](https://github.com/votingworks/vxsuite/blob/v4.1.1/libs/auth/src/cast_vote_record_hashes.ts) — CVR hashing logic, including the Merkle tree implementation
