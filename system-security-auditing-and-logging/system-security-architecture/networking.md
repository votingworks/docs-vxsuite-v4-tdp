# Networking

All VxSuite components are blocked from connecting to any network. Thus, there is no networking in a VxSuite implementation. Our network design is secure by virtue of it being completely absent.

Networking is disabled through several layers of defense:

* Network drivers and known network connections are purged in the software setup process. See the [setup-machine.sh](https://github.com/votingworks/vxsuite-complete-system/blob/ea6b16374f7f8a35e1f4fa6a0291291987e925cb/setup-machine.sh#L422) script.
* Secure boot ensures that the hard drive is not modified, thus preventing software that isn’t part of the approved VotingWorks bundle from running.
* The network stack is disabled in the BIOS.
* Wi-fi or bluetooth hardware is not present on the machines.
* Ethernet ports are blocked.

Because there is no networking, all electronic data transfer is air-gapped via USB flash drives.
