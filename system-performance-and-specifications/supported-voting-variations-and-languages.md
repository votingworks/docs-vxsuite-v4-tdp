# Supported Voting Variations & Languages

## Supported Voting Variations

### Supported Contest Types

* N-of-M contests, which are typically candidate contests
* Yes-No contests, also known as ballot propositions or ballot measures
* Straight party contests, in which the voter chooses a party. Candidates of the selected party receive "indirect votes" even if no "direct vote" (i.e. mark) was made for those candidates.

### Supported Election Types

* Standard general elections, in which each political subdivision has a single ballot style with contests that are not party-specific. Maps to `general` in the VxSuite election definition.
* Standard primary elections, in which each political subdivision has a ballot style for each party included in the primary. These elections may be either "open" or "closed" primaries, depending on the jurisdiction's rules on how voters choose a party or ballot. Maps to `closed-primary` in the VxSuite election definition.
* Consolidated ballot open primary elections, in which each political subdivision has a single ballot style that contains primary contests from multiple parties. The voter votes in no more than one party's set of contests on the ballot. The purpose of a consolidated primary ballot is, in part, to allow the voter to privately choose their party. Maps to `open-primary` in the VxSuite election definition.

## Supported Languages

* English
* Spanish
* Chinese (Simplified & Traditional)

Voter-facing content in an election package can be translated to additional left-to-right languages and imported into VxSuite, but is not formally supported or tested by VotingWorks.
