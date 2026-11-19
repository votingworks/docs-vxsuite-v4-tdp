# Networking

All VotingWorks applications are blocked from connecting to any external network, by default. The VxAdmin application does allow local networking when using multi-station adjudication, and the VxCentralScan application allows local networking to send cast vote records (CVRs) to a host VxAdmin.

In all VotingWorks applications, except for VxAdmin and VxCentralScan, networking of any kind is disabled through several layers of defense:

* Unless a system is running the VxAdmin or VxCentralScan application, VotingWorks removes all networking packages and disables any related networking services. These actions are defined in [setup-machine.sh](https://github.com/votingworks/vxsuite-complete-system/blob/v4.1.1/setup-machine.sh#L336).
* Secure Boot, together with dm-verity verification of the read-only partition, prevents a machine with a modified hard drive from booting, so software that is not part of the approved VotingWorks bundle does not run.
* The network stack is disabled in the BIOS.
* Wi-Fi or Bluetooth hardware is not present on the machines.
* Ethernet ports are blocked.
* As a final layer of defense, a [firewall configuration](https://github.com/votingworks/vxsuite-build-system/blob/v4.1.1/playbooks/trusted_build/firewalld.yaml) is defined to block any incoming or outgoing traffic in the event that a connection is created by other means.
* Because there is no networking on these applications, all electronic data transfer from them is air-gapped via USB drives.

For VxAdmin and VxCentralScan systems, local networking over a wired Ethernet connection is possible: on VxAdmin for multi-station adjudication, and on VxCentralScan for sending CVRs to a host VxAdmin. To ensure the integrity of this system, multiple layers of defense are used:

* By default, local networking services are disabled. That configuration is defined in [local\_ethernet\_config.yaml](https://github.com/votingworks/vxsuite-build-system/blob/v4.1.1/playbooks/trusted_build/local_ethernet_config.yaml)
* Only VotingWorks turns on local networking, for a VxAdmin or a VxCentralScan, through the basic configuration wizard or the vendor menu. The setting persists across software installations.
* A VxAdmin or VxCentralScan system with local networking turned on only allows local Ethernet connections, as defined in [the systemd network configuration](https://github.com/votingworks/vxsuite-build-system/blob/v4.1.1/playbooks/trusted_build/files/10-ethernet.network).
* To authorize local network connections, each system must contain a valid strongSwan configuration. The strongSwan configuration consists of certificate-based authentication tied to the Trusted Platform Module (TPM), which is unique to each VotingWorks system. That certificate creation and initial validation can be found in [generate-key.sh](https://github.com/votingworks/vxsuite-complete-system/blob/v4.1.1/config/vendor-functions/generate-key.sh) and [create-machine-cert.sh](https://github.com/votingworks/vxsuite-complete-system/blob/v4.1.1/config/vendor-functions/create-machine-cert.sh)
* The strongSwan configuration that enforces the use of these certificates can be found in [vxswan.conf](https://github.com/votingworks/vxsuite-build-system/blob/v4.1.1/playbooks/trusted_build/files/vxswan.conf)
* In multi-station mode, the host announces itself on the local network with multicast DNS (mDNS) using `avahi`. Adjudication stations and networked VxCentralScans use the announcement only to find the host; all other traffic between machines on the local network is carried over the authenticated strongSwan connection.
* At the application layer, a VxAdmin only forms adjudication connections with peers running an identical software version. A host [rejects any station that reports a mismatched code version](https://github.com/votingworks/vxsuite/blob/v4.1.1/apps/admin/backend/src/peer_app.ts), and a station independently refuses to connect to a host running an incompatible version, so a machine that reports a different software version is not admitted to the adjudication network. A VxCentralScan likewise sends CVRs only when it finds exactly one host, running the same software version and configured for the same election.
* The same firewall configuration that is present on systems without networking is also used on VxAdmin and VxCentralScan systems to prohibit any external network access.
