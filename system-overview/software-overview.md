# Software Overview

VotingWorks software is open-source, which means that the code is free and publicly available. All code written by VotingWorks and almost all dependencies are open-source, with the notable exception of third-party firmware for various hardware components.&#x20;

All system components - VxAdmin, VxMark, VxScan, and VxCentralScan - run different application code but have fundamentally the same software architecture. The rest of this document applies to all system components unless otherwise noted.

## Operating System

The system uses [Debian](https://www.debian.org/) 12 as the base operating system. Debian is a free and open source Linux distribution developed by the Debian Project. The operating system is first installed with the minimally required dependencies and then any additional packages required by the system are installed during build time.

Due to the extensive security measures, users are limited to using the application software and will not have access to Debian's typical set of features.

## Application Architecture

<figure><img src="../.gitbook/assets/image (63).png" alt="" width="563"><figcaption><p>Application architecture diagram</p></figcaption></figure>

All machines are completely disconnected from any network and have network capabilities disabled, but the frameworks and architecture employed are borrowed from web-based development. The user interacts with a restricted browser which communicates with a server that provides the web-content and another server that provides application data and hardware status.&#x20;

### Kiosk Browser

The kiosk browser is a web browser restricted to rendering a single full-screen application. The code can be found in the [kiosk-browser repository](https://github.com/votingworks/kiosk-browser) **(update link)**. It is a thin [Electron](https://www.electronjs.org/) application which uses [Chromium](https://www.chromium.org/chromium-projects/) as its rendering engine. The browser communicates with the frontend server which serves HTML, JavaScript, and assets. The browser also communicates with the backend server which serves application data. Electron enables the browser to access certain operating system APIs - such as open file dialogs - that a lone renderer would not have access to. The browser is launched at startup, with limited privileges, and cannot be exited. Everything a standard (non-vendor) user sees or does is mediated through the kiosk browser.

### Application Frontend Server

The frontend is a [React](https://react.dev/) application served from a [Node.js](https://nodejs.org/en) server. All code for the application frontends are in the [vxsuite repository](https://github.com/votingworks/vxsuite).

### Application Backend Server

The application backend is a separate [Node.js](https://nodejs.org/en) server which acts as the core of the entire application in that it manages all persistent data and communication with peripherals. All code for the application backends are in the [vxsuite repository](https://github.com/votingworks/vxsuite). Most code is written in Typescript but some performance sensitive code, such as interpretation and background daemons, are written in [Rust](https://www.rust-lang.org/) and executed as binaries at runtime.

#### Application Data Management

All application data that persists across restarts is stored or tracked in a [SQLite](https://www.sqlite.org/) database. Each machine has a single database that the application backend accesses to update or retrieve data such as election configuration, cast vote record data, diagnostic data, etc. Logging data is a notable exception that is stored outside of the application databases.

#### Peripheral Management

The hardware peripherals are polled and managed through the application backends. For example when detecting the status of the card reader, the browser polls the backend server which in turn polls the hardware itself and returns a status to the browser. In order to manage changing states of more complex hardware such as scanners, the backends use state machines.

The exact layer between the application backend and the hardware varies by hardware. Some run in-process whereas others run as a separate process with which the backend communicates. For the accessibility peripherals - the accessible controller and the sip-and-puff interface - the backend starts and manages a daemon which surfaces user input directly to the browser as keyboard commands.&#x20;

In many cases VotingWorks has written custom drivers that interface directly with the USB device. In other cases, VotingWorks leverages open-source middleware layers installed as Debian packages:

<table><thead><tr><th width="177">Machine</th><th width="198">Peripheral</th><th>Middleware Source</th></tr></thead><tbody><tr><td>All</td><td>Card Reader</td><td><a href="https://pcsclite.apdu.fr/">PCSC lite</a></td></tr><tr><td>VxScan</td><td>Scanner</td><td>VotingWorks</td></tr><tr><td>VxScan</td><td>Printer</td><td>VotingWorks</td></tr><tr><td>VxMark</td><td>Printer-Scanner</td><td>VotingWorks</td></tr><tr><td>VxMark</td><td>Accessible Controller</td><td>VotingWorks</td></tr><tr><td>VxMark</td><td>Sip and Puff</td><td>VotingWorks</td></tr><tr><td>VxAdmin</td><td>Printer</td><td><a href="https://www.cups.org/">CUPS</a></td></tr><tr><td>VxCentralScan</td><td>Scanner</td><td><a href="http://www.sane-project.org/">SANE</a></td></tr></tbody></table>

Firmware for embedded devices such as screens and speakers is bundled with the operating system.

## Software Independence

The voting system achieves software independence through the use of independent voter-verifiable paper records. All ballots are voter-verified paper ballots, either [hand marked ballots](hand-marked-ballots.md) or [machine marked ballots](machine-marked-ballots.md).

On hand marked paper ballots, voters fill in bubbles next to their selections. Because voter indications are made and reviewed directly by the voter, they are inherently voter-verified. The software interprets the image of the ballot for tabulation but, of course, the paper ballot persists after scanning.

For machine marked paper ballots, voters make selections on screen at VxMark. After the voter has made all their selections, the ballot is printed and presented to the voter. The ballot displays a textual representation of the selections and a QR code with the selections encoded. The voter reviews the ballot and, once accepted, the voter-verified ballot is ejected into the attached ballot box. VxMark's machine marked ballots are not actually tabulated until they are scanned at a scanner.

Ballots are never modified by the system after voter verification in any way that could affect voter selections or the ability to perform an audit. The only modification to ballots is the possible use of an imprinter on VxCentralScan, which prints only an identifier along the outside margin of the ballot.

Because all voter selections are recorded on paper, voter-verified, and unmodified, the election results can always be re-tabulated or audited.

## Lack of Network Connectivity

All machines do not and cannot connect to any network at any time. Networking is disabled in a multi-layered approach:

* **Hardware** - Wireless network chips are not installed, preventing the device from accessing wireless networks. On devices with an ethernet port, a port blocker is installed.
* **BIOS -** The networking stack is disabled at the BIOS level.
* **Operating System** - All network drivers are purged from the system when the software image is locked down.

Because there is no networking, all electronic data transfer takes place via USB flash drives.

## Key VotingWorks Repositories

There are four code repositories relevant to the voting system:

* [vxsuite](https://github.com/votingworks/vxsuite) - all application code and supporting libraries
* [kiosk-browser](https://github.com/votingworks/kiosk-browser) - kiosk browser code
* [vxsuite-complete-system](https://github.com/votingworks/vxsuite-complete-system) - installation code and configuration
* [vxsuite-build-system](https://github.com/votingworks/vxsuite-build-system/tree/main) - image creation and dependency management

## Key Dependency Chart

<table><thead><tr><th width="293">Dependency</th><th>Version</th></tr></thead><tbody><tr><td>Debian</td><td>12.2.0</td></tr><tr><td>Additional Debian Packages</td><td>See <a href="https://github.com/votingworks/vxsuite-build-system/blob/main/inventories/v3.1/group_vars/all/packages.yaml">build system package inventory</a> (<strong>update link</strong>)</td></tr><tr><td>Node.js</td><td>20.16.0</td></tr><tr><td>pnpm</td><td>8.15.5</td></tr><tr><td>Application Node Packages</td><td>See the relevant <a href="https://github.com/votingworks/vxsuite/blob/main/pnpm-lock.yaml">lock file</a> (<strong>update link</strong>)</td></tr><tr><td>Rust</td><td>1.81</td></tr><tr><td>Rust Packages</td><td>See the relevant <a href="https://github.com/votingworks/vxsuite/blob/main/Cargo.lock">lock file</a> <strong>(update link)</strong></td></tr><tr><td>yarn</td><td>1.22.22</td></tr><tr><td>Electron</td><td>17.4.1</td></tr><tr><td>Chromium</td><td>98.0.4758.141</td></tr><tr><td>Kiosk Browser Node Packages</td><td>See the relevant <a href="https://github.com/votingworks/kiosk-browser/blob/main/yarn.lock">lock file</a> (<strong>update link</strong>)</td></tr></tbody></table>

## Software Traceability

**NEED TO WRITE**

## Common Software Functions

Subsequent articles will describe the particular software design of each application, but some software patterns are common across all applications and described here.

### USB Management

All VxSuite components require a USB drive at some point in their operation for configuration or for the import or export of results. The application is polling for attached USB drives multiple times per second. If a USB drive with a FAT32 partition is detected, the application will attempt to mount the USB drive to a known mount point. Once mounted, the USB drive will be available for use by the application.

The USB drive should be ejected before removing it. Most critical operations also make sure to sync the data to the USB drive before allowing the user to continue, however, so removing the USB drive without ejecting will normally not result in problems.

Only one USB drive can be used at a time and additional USB drives inserted after the first USB drive will be ignored.

### Document Creation

All VxSuite components must generate documents for printing or export. VxAdmin and VxScan must generate tally and ballot count reports. All components must generate diagnostic readiness reports.&#x20;

In order to do so, the applications have a headless browser (specifically Chromium) launched by the backend. Exported documents are all defined in terms of HTML (using React), so the headless browser is able to load the documents and render them as PDFs. The PDFs can then be sent to printer or saved to a USB drive.

### Date & Time Management

The date and time is set on the machine in during initial configuration before the machine is sent to a customer. There is some amount of "clock drift" over time for all computers, however, so eventually the clocks may be wrong. This may cause problems with authentication due to mismatched timestamps and will cause reports to have incorrect timestamps.

All machines allow system administrators and election managers to edit the date, time, and time zone in order to address clock drift or, in rare cases, to set up machines for use in a part of the jurisdiction with different time settings.

{% hint style="info" %}
**User Manual Reference**: [Setting Date & Time](https://app.gitbook.com/s/JtZutzGTdCzsGITrdiph/vxadmin-system-setup/setting-date-and-time "mention")
{% endhint %}

### Other

* [ballot-interpretation.md](ballot-interpretation.md "mention")
* [diagnostics.md](diagnostics.md "mention")
