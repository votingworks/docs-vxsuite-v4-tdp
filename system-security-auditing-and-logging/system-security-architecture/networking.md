# Networking

All VotingWorks applications are blocked from connecting to any external network, by default. The VxAdmin application does allow local networking when using multi-station adjudication.

In all VotingWorks applications, except for VxAdmin, networking of any kind is disabled through several layers of defense:

* Unless a system is running the VxAdmin application, we remove all networking packages and disable any related networking services. You can see these actions in [setup-machine.sh](https://github.com/votingworks/vxsuite-complete-system/blob/main/setup-machine.sh#L336).&#x20;
* Secure boot ensures that the hard drive is not modified, thus preventing software that isn’t part of the approved VotingWorks bundle from running.&#x20;
* The network stack is disabled in the BIOS.
* Wi-fi or bluetooth hardware is not present on the machines.
* Ethernet ports are blocked.
* As a final layer of defense, a [firewall configuration](https://github.com/votingworks/vxsuite-build-system/blob/main/playbooks/trusted_build/firewalld.yaml) is defined to block any incoming or outgoing traffic in the event a connection was somehow created.
* Because there is no networking on non-VxAdmin applications, all electronic data transfer is air-gapped via USB drives.

For VxAdmin systems, local networking over a wired Ethernet connection is possible when using multi-station adjudication. To ensure the integrity of this system, multiple layers of defense are used:

* By default, local networking services are disabled. You can see that configuration in [local\_ethernet\_config.yaml](https://github.com/votingworks/vxsuite-build-system/blob/main/playbooks/trusted_build/local_ethernet_config.yaml)
* A VxAdmin system with multi-station adjudication enabled only allows local ethernet connections, which can be seen in [the systemd network configuration.](https://github.com/votingworks/vxsuite-build-system/blob/main/playbooks/trusted_build/files/10-ethernet.network)
* To authorize local network connections, each system must contain a valid strongSwan configuration. The strongSwan configuration consists of certificate-based authentication tied to the TPM, which is unique to each VotingWorks system. That certificate creation and initial validation can be found in [generate-key.sh](https://github.com/votingworks/vxsuite-complete-system/blob/main/config/vendor-functions/generate-key.sh) and [create-machine-cert.sh](https://github.com/votingworks/vxsuite-complete-system/blob/main/config/vendor-functions/create-machine-cert.sh)
* The strongSwan configuration that enforces the use of these certificates can be found in [vxswan.conf](https://github.com/votingworks/vxsuite-build-system/blob/main/playbooks/trusted_build/files/vxswan.conf)
* At the application layer, a VxAdmin only forms adjudication connections with peers running an identical software version. A host [rejects any station that reports a mismatched code version](https://github.com/votingworks/vxsuite/blob/main/apps/admin/backend/src/peer_app.ts), and a station independently refuses to connect to a host running an incompatible version, so a machine running different or modified software cannot join the adjudication network.
* The same firewall configuration that is present on non-VxAdmin systems is also used on VxAdmin systems to prohibit any external network access.&#x20;
