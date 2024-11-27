# Hash/Checksum Verification of Dependencies

The VotingWorks build system, [vxsuite-build-system](https://github.com/votingworks/vxsuite-build-system/tree/v4.0.0), utilizes many different tools to install, configure, and build VotingWorks applications. To ensure the integrity of the build system and tools used, all third-party tools are verified against known hashes, checksums, or digital signatures. This appendix provides a description of the mechanism used to verify each tool and any additional resources those tools may be responsible for providing during the build process.

**APT**

Debian's package manager, apt, is built on a secure framework described here: [SecureApt](https://wiki.debian.org/SecureApt).

The VotingWorks build process relies on this fundamental tool to install many of the system level tools required to build our applications. As an added measure of security, all packages are pinned to specific versions to ensure a consistent build environment over time.

To further ensure that consistent versions of dependencies and transitive dependencies are used, we create our own VotingWorks-hosted apt snapshot to pull from.

**pip**

Python's package manager, pip, does not verify package integrity by default. However, secure installation is possible via the method described here: [pip: Secure installs](https://pip.pypa.io/en/stable/topics/secure-installs/).

The VotingWorks build process implements the above method in the [tb-install-ansible.sh](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/scripts/tb-install-ansible.sh) script. The required packages are listed, along with their hash, in unique requirements files based on the operating system version and architecture. You can see an example here: [Debian 12 x86 pip requirements](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/scripts/pip_deb12_x86_64_requirements.txt).

**RubyGems**

Ruby's package manager, gem, does not verify package integrity by default. However, the official gem repository provides SHA256 checksums for hosted packages. You can see an example here: [FPM 1.15.1](https://rubygems.org/gems/fpm/versions/1.15.1).

The VotingWorks build process requires the version and SHA256 checksum for any installed gems. Once the gem file has been downloaded, it is checked against this checksum to verify its integrity. You can see that checksum verification in the rubygems playbook here: [rubygems.yaml](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/playbooks/trusted_build/rubygems.yaml).

**Rust**

By default, Rust is installed over an active internet connection. Since that method is not available during the offline phase of the VotingWorks build process, we use a standalone, offline installer binary provided by Rust. To verify the integrity of the installer, the downloaded file is verified against the officially published checksum that can be found in each version's official manifest. You can see that checksum verification in the rust playbook here: [rust.yaml](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/playbooks/trusted_build/rust.yaml).

**Cargo**

Cargo is the Rust package manager. It provides secure installs via the combination of a manifest listing packages and their versions, along with a lock file containing the checksum for each package. That method is described here: [Cargo.toml vs. Cargo.lock](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html).

**Node**

Node is typically installed via package managers like apt, or via a direct install from a specific version. We do not install Node via apt since we explicitly version it. As a result, we download the appropriate installer from the official Node repository. That downloaded file is then checked against the officially provided checksum. You can see that checksum verification in the node playbook here: [node.yaml](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/playbooks/trusted_build/node.yaml).

**npm**

npm is the default Node package manager. It is installed as part of the Node install previously described.

Packages installed via npm are checked against the officially provided checksums for each package. You can see that checksum verification in the node playbook here: [node.yaml](https://github.com/votingworks/vxsuite-build-system/blob/v4.0.0/playbooks/trusted_build/node.yaml).

**pnpm**

pnpm is another package manager for the Node ecosystem. It is installed via npm as previously described to ensure its integrity.

Packages installed via pnpm use a lockfile: pnpm-lock.yaml. This lockfile includes the version and checksum to verify integrity when packages are installed during the build process. In addition, the VotingWorks build process explicitly requires the use of `--frozen-lockfile` to ensure that only the packages explicitly required are installed.

**Yarn**

Yarn is another package manager for the Node ecosystem. It is installed via npm as previously described to ensure its integrity.

Packages installed via yarn use a lockfile: yarn.lock. This lockfile includes the version and checksum to verify integrity when packages are installed during the build process. In addition, the VotingWorks build process explicitly requires the use of `--frozen-lockfile` to ensure that only the packages explicitly required are installed.
