# Software Installation Record Creation

When installing VotingWorks applications that will be used in one or more elections, it is necessary to create a record of the software installation. There are multiple requirements, as described below.&#x20;

3.1.4-I.1 a unique identifier (such as a serial number) for the record;\
3.1.4-I.2 a list of unique identifiers of storage media associated with the record;\
3.1.4-I.3 the time, date, and location of the software installation;\
3.1.4-I.4 names, affiliations, and signatures of all people present;\
3.1.4-I.5 copies of the procedures used to install the software on the programmed devices of the voting system;\
3.1.4-I.6 the certification number of the voting system;\
3.1.4-I.7 list of the software installed as well as associated digital signatures and mechanisms for installation and verification on programmed devices of the voting system; and\
3.1.4-I.8 a unique identifier (such as a serial number) of the vote-capture device or election management system (EMS) which the software is installed.

To satisfy the above requirements, VotingWorks recommends following these best practices related to each requirement.&#x20;

3.1.4-I.1 - We recommend using the machine ID for this record, e.g. `SC-11-004` If necessary, appending the install date and time can further ensure uniqueness, e.g. `SC-11-004-20250325-1300`

3.1.4-I.2 - This should be the machine ID + the system drive the application was installed to. For example, a machine identified as `SC-11-004` with the VotingWorks application installed to the `/dev/nvme0n1` drive would use the record: `SC-11-004-dev-nvme0n1`

3.1.4-I.3 - As described.

3.1.4-I.4 - As described.

3.1.4-I.5 - Include physical copies of the TDP install instructions or a link to the TDP install instructions for this release.

3.1.4-I.6 - This is the EAC Certification Number, which can be found on the Certificate of Conformance for this VotingWorks application release.

3.1.4-I.7 - Include a physical copy of the COTS Report or a link to the COTS Report that can be found in the [hash-checksum-verification-of-dependencies.md](../trusted-build/hash-checksum-verification-of-dependencies.md "mention")documentation, specific to each VotingWorks application release.

3.1.4-I.8 - We recommend using the serial number of the hardware device the VotingWorks application is being installed to. If that is not available, the same identifier used in 3.1.4-I.1 is recommended.&#x20;
