# Build Machine Configuration

## Build Machine Requirements <a href="#build-machine-requirements" id="build-machine-requirements"></a>

* Operating system: Debian 12
* RAM: 8GB minimum
* Chip: x86-64 / amd64 CPU architecture, Intel i5 or higher
* Storage: 250GB minimum

## Build Machine Configuration <a href="#build-machine-configuration" id="build-machine-configuration"></a>

Debian 12 will need to be installed on the build machine. You can find detailed instructions for that process under [Installing Debian 12 on VxBuild](installing-debian-12-on-vxbuild.md). Once that is complete, we can install the VotingWorks build system, [vxsuite-build-system](https://github.com/votingworks/vxsuite-build-system).

Throughout the rest of this document, substitute `<inventory-name>` with the inventory provided by VotingWorks.

```
sudo apt install -y git
mkdir ~/code && cd ~/code
git clone https://github.com/votingworks/vxsuite-build-system

cd ~/code/vxsuite-build-system
./scripts/tb-initialize-build-machine.sh <inventory-name>
./scripts/tb-clone-images.sh <inventory-name>
```

At this point, you should have three separate VMs: `debian-<inventory-name>-<apt-snapshot-name>`, `online`, and `offline`. You can confirm this by running:

```
sudo virsh list --all
```
