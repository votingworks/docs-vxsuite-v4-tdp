# Build Machine Configuration

## Build Machine Requirements <a href="#build-machine-requirements" id="build-machine-requirements"></a>

* Operating system: Debian 12
* RAM: 8 GB minimum
* Chip: x86-64 / amd64 CPU architecture, Intel i5 or higher
* Storage: 250 GB minimum

## Build Machine Configuration <a href="#build-machine-configuration" id="build-machine-configuration"></a>

Debian 12 must be installed on the build machine, as described under [Installing Debian 12 on VxBuild](installing-debian-12-on-vxbuild.md).

Throughout the rest of this document, substitute `<version>` with the version string provided by VotingWorks, e.g., `v4.1.1`.

To install the VotingWorks build system, [vxsuite-build-system](https://github.com/votingworks/vxsuite-build-system/tree/v4.1.0), run the following commands:

```
sudo apt install -y git
mkdir ~/code && cd ~/code
git clone https://github.com/votingworks/vxsuite-build-system

cd ~/code/vxsuite-build-system
git checkout main
git pull
git checkout <version>
./scripts/tb-initialize-build-machine.sh stable
./scripts/tb-clone-images.sh stable
```

The build machine now has two separate virtual machines (VMs): `debian-<version>-<apt-snapshot-date>-<debian-release-name>` and `online`. To confirm this, run:

```
sudo virsh list --all
```
