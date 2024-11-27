# Hashing of Continuously Exported Cast Vote Records

## Continuous Export

Our precinct scanners export cast vote records (CVRs) to USB drive continuously, as ballots are cast. Continuous export also allows for a speedy polls close, as cast vote records need not be exported all at once on polls close.

## Merkle Tree Structure

To perform continuous export while also keeping signatures, i.e., authenticity information, up-to-date, we have to be able to write both CVRs and authenticity information incrementally. (It isn’t enough to just hash and sign new data. We need an up-to-date root hash/signature.) We can use a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) structure to accomplish this efficiently.

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Assuming every CVR has a random UUID, e.g. 4d6a9dad-e6d6-4a29-89bc-9ab915012b73, we can specifically use the following structure:

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

### In Practice

We don’t actually have to 1) use a nested directory structure on the USB or 2) store all intermediate hashes on the USB. We can store the structure and intermediate hashes on the machine in a database table, e.g.

| CVR ID Prefix 1 | CVR ID Prefix 2 | CVR ID                               | Hash                                      |
| --------------- | --------------- | ------------------------------------ | ----------------------------------------- |
| -               | -               | -                                    | Root hash                                 |
| 4               | -               | -                                    | 4 hash                                    |
| 4               | 4d              | -                                    | 4d hash                                   |
| 4               | 4d              | 4d6a9dad-e6d6-4a29-89bc-9ab915012b73 | 4d6a9dad-e6d6-4a29-89bc-9ab915012b73 hash |
| …               |                 |                                      |                                           |

Then on the USB, we can use a flat structure that’s much easier to reason about and iterate over:

```
<cvr-directory-name>.vxsig ← Signature on root-hash.txt
<cvr-directory-name>/
  root-hash.txt
  4d6a9dad-e6d6-4a29-89bc-9ab915012b73/
    cast-vote-record-report.json
    Images
```

The database table makes recomputing hashes easy, as retrieval of all hashes for a given ID prefix becomes a simple SQL query. This approach also decreases the chance that we accidentally depend on data written to the USB drive when computing hashes, protecting against [compromised or faulty USB drives](https://github.com/votingworks/vxsuite/pull/3554).

In the above examples, we’ve listed a root-hash.txt file and have signed that. In practice, we use a JSON file capable of storing other metadata and sign that:

```
<cvr-directory-name>.vxsig ← Signature on metadata.json
<cvr-directory-name>/
  metadata.json
  4d6a9dad-e6d6-4a29-89bc-9ab915012b73/
    cast-vote-record-report.json
    Images
```

Sample metadata.json:

```
{
  "arePollsClosed": false,
  "castVoteRecordRootHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  ...
}
```

## Import

Whenever a machine imports a CVR directory, it authenticates the CVRs by 1) verifying the signature on the metadata.json file and 2) recomputing the “castVoteRecordRootHash” in metadata.json from scratch to ensure that it’s correct.

## Code Links

Refer to the following code links for more details:

* [https://github.com/votingworks/vxsuite/blob/v4.0.0-release-branch/libs/auth/src/cast\_vote\_record\_hashes.ts](https://github.com/votingworks/vxsuite/blob/v4.0.0-release-branch/libs/auth/src/cast_vote_record_hashes.ts) — CVR hashing logic, including the Merkle tree implementation
