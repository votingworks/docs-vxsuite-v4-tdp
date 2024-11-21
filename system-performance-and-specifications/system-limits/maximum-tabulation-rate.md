# Maximum Tabulation Rate

##

The maximum tabulation rate for batch-fed scanners is primarily limited by the hardware scanning speed limit for each central scanner model:

* Ricoh fi-8170: 80 sheets per minute
* Ricoh fi-7600: 100 sheets per minute

The sheet per minute rate is reduced by the need to interpret ballot images. Ballot interpretation speed varies based on the following ballot variables:

* Ballot type
  * Ballot marking device ballots are slower to interpret than hand marked paper ballots.
* Sheet length
  * Shorter (such as 11") ballots are faster to interpret than longer (such as 22") ballots.
* Ballot content
  * Ballots with more contests and contests selections are slower to interpret.

Taking these limitations into consideration, batch scanners can be expected to scan approximately 50 sheets per minute for typical elections configurations.

In addition to the sheet per minute rate of a given batch, the maximum tabulation rate is also limited by the maximum batch size for each scanner. Due to the paper weight range supported by VxSuite, VotingWorks recommends a smaller batch size than the original manufacturer recommendation:

* Ricoh fi-8170: 30 sheets per batch
* Ricoh fi-7600: 100 sheets per batch

Finally, the maximum tabulation rate over the course of a day is limited by the daily volume limitations of each central scanner:

* Ricoh fi-8170: 10,000 sheets/day
* Ricoh fi-7600: 44,000 sheets/day

