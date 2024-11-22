# Networking

All VxSuite components are blocked from connecting to any network. Thus, there is no network in a VxSuite implementation. Our network design is secure by virtue of it being completely absent.

We ensure that VxSuite components cannot connect to a network, either wifi, bluetooth, or ethernet. This is achieved through a few layers of defense:

* Networking manager is turned off and removed in the setup process. See `vxsuite-complete-system/setup-machine.sh`
* Secure boot ensures that the hard drive is not modified, thus preventing software that isn’t part of the approved VotingWorks bundle from running.
* The BIOS is configured to disallow network connections.
* Wifi/bluetooth hardware is not present on the machines.
