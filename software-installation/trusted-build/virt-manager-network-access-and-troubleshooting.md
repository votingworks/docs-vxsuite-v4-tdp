# Virt Manager - Network Access & Troubleshooting

### Disabling Network Access <a href="#disabling-network-access" id="disabling-network-access"></a>

By default, newly created VMs have networking enabled. To ensure the offline VM does not have access to the internet, the networking link is disabled before the VM is ever used. This is accomplished by editing the VM's configuration (found in /etc/libvirt/qemu/offline.xml) and setting the link state to down. This functionality can be seen in the vxsuite-build-system repo, in [playbooks/virtmanager/clone-base-vm.yaml](https://github.com/votingworks/vxsuite-build-system/blob/main/playbooks/virtmanager/clone-base-vm.yaml).

If an offline VM exists, the XML configuration file is updated to set the link state to down. After that, the offline VM is explicitly re-defined from this updated XML configuration file. These steps always execute, even if the network link state is already set to down.

Any VM cloned from this offline VM will also have a disabled network since those settings are inherited from the original VM.

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

Virt Manager uses a local bridge network to connect to VMs. If you receive an error when starting a VM that says "Error starting domain: Cannot get interface MTU on 'virbr0': No such device", run the following command in the terminal on the build machine:

```
sudo virsh net-start default
```

You should now be able to return to the VM and start it without issue.
