# System Performance & Specifications

## Supported Voting Variations

* N-of-M contests
* Yes/No contests
* Partisan Primary Elections
  * The voting system itself does not have a concept of an open vs. closed primary as primary ballot styles are restricted to one party, but can support both types of primaries through procedurally restricting a voter to a given ballot style.

## Supported Languages

* English
* Spanish
* Chinese (Simplified & Traditional)

Voter-facing content in an election package can be translated to additional left-to-right languages and imported into VxSuite, but is not formally supported or tested by VotingWorks.

## Maximum Tabulation Rate

The maximum tabulation rate for batch-fed scanners is primarily limited by the hardware scanning speed limit for each central scanner model:

* Ricoh fi-8170: 80 sheets per minute
* Ricoh fi-7600: 100 sheets per minute

The sheet per minute rate is reduced by the following ballot variables that influence the speed of software ballot interpretation:

* Ballot type
  * Ballot marking device ballots are faster to interpret than hand marked paper ballots.
* Sheet length
  * Shorter (such as 11") ballots are faster to interpret than longer (such as 22") ballots.
* Ballot content
  * Ballots with more contests and contests selections are slower to interpret.

In addition to the sheet per minute rate of a given batch, the maximum tabulation rate is also limited by the maximum batch size for each scanner. Due to the paper weight range supported by VxSuite, VotingWorks recommends a smaller batch size than the original manufacturer recommendation:

* Ricoh fi-8170: 30 sheets per batch
* Ricoh fi-7600: 100 sheets per batch

##









