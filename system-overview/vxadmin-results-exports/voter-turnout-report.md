# Voter Turnout Report

The voter turnout report shows the turnout of the election by precinct. The turnout is calculated as the number of ballots divided by the number of registered voters per precinct.

<figure><img src="../../.gitbook/assets/vxadmin-voter-turnout-report-printed.png" alt="Printed voter turnout report listing ballots cast, registered voters and turnout percentage by precinct" width="375"><figcaption></figcaption></figure>

The number of registered voters per precinct is pulled from the `registeredVoterCounts.json` in the election package. If the file is not included in the election package, the report is not available on VxAdmin.
