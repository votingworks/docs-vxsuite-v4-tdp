# VxAdmin & VxCentralScan Maintenance Manual

## Laptop Maintenance

VxAdmin & VxCentralScan are simply COTS laptops that are sealed and installed with VotingWorks software. For reference information, see the following links:

* **Hardware Overview -** [#laptop](../system-overview/vxadmin-and-vxcentralscan-hardware.md#laptop "mention")
* **Software Functionality -** [vxadmin-function.md](../system-overview/vxadmin-function.md "mention") & [vxcentralscan-function.md](../system-overview/vxcentralscan-function.md "mention")
* [**Manufacturer Datasheet**](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-elitebook-840-14in-g11/hp-elitebook-840-14in-g11-datasheet.pdf)
* [**Manufacturer User Guide**](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-elitebook-840-14in-g11/hp-elitebook-840-14in-g11-user-guide.pdf)

### Hardware Maintenance

There is no required hardware maintenance for the laptop. The end user should never remove the bottom panel of the laptop for maintenance. The bottom panel is sealed by VotingWorks. Additionally, the BIOS is configured to enable "Cover Removal Detection" which means that removing the bottom panel will be trigger a sensor and will prevent the computer from subsequently booting without a VotingWorks managed password. As a result, any end user attempt to service their own laptop will result in making the laptop unusable until it is fixed by VotingWorks. Instead of ever servicing the laptop themselves, end users should report hardware issues directly to VotingWorks to resolve. Hardware issues may include, for example, a screen with defects, a battery that does not charge, or an undetected smart card reader.

VotingWorks recommends cleaning the screen and keyboard as needed. The screen can be cleaned by gently wiping with cleaning wipes such as ULINE S-12236 or equivalent. The keyboard can be cleaned by blowing the keyboard with air in a can, such as ULINE S-6771 or equivalent, from a distance of at least one foot. Read all manufacturer safety instructions before using air in a can.

### Software Maintenance

There are no required steps for maintaining the software or firmware itself. The software is installed by VotingWorks and cannot be modified. The underlying databases for all applications are self-maintaining and do not need to be tuned by end users.

### Data Maintenance

As VxAdmin and VxCentralScan are used for an election, they will gradually be storing more and more data. VxCentralScan stores ballot images and interpretations for all scanned ballots and VxAdmin stores imported cast vote records, which often include images as well. It is the responsibility of the election manager using VxAdmin and VxCentralScan to monitor data usage.&#x20;

The free disk space available on VxAdmin and VxCentralScan is visible to system administrators and election managers under the **Diagnostics** menu accessible from the application sidebar when authenticated. When free disk space hits 0%, the application is no longer able to add data, whether that's in the form of a scanned ballot or imported CVRs. As long as users remain within the specified[system-limits](../system-performance-and-specifications/system-limits/ "mention") they should not hit 0%.

When the machine is unconfigured or ballot data is cleared, disk space will be recovered. It will likely not return all the way to 100% free disk space, due to how the database is configured to vacuum only as needed, but all disk space from deleted records will be usable for new records.

VotingWorks recommends that all scanned ballot data is backed up from VxCentralScan to a USB drive before being cleared from the application. The application forces the user to perform the backup. VotingWorks recommends a 64GB SanDisk Ultra Flair USB 3.0 Drive (PN: SDCZ73-064G-G46) for most operations and the faster 128GB SanDisk Extreme PRO USB 3.2 Drive (PN: SDCZ880-128G-G46) for very large backups. See user manual instructions [Retaining and Removing Files - VxCentralScan](https://app.gitbook.com/s/JtZutzGTdCzsGITrdiph/vxcentralscan/retaining-and-removing-files-vxcentralscan "mention")for details.&#x20;

## VxAdmin Printer Maintenance

VxAdmin is accompanied by a HP LaserJet Pro 4001dn printer which enables printing reports. The [manufacturer specifications ](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-laserjet-pro-4001dn/hp-laserjet-pro-4001dn-datasheet.pdf)and [manufacturer user guide ](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-laserjet-pro-4001dn/hp-laserjet-pro-4001dn-user-guide.pdf)are included in the documentation repository.&#x20;

### Paper Specifications

VotingWorks recommends using only the printer's Tray 2, which is the bottom, higher capacity tray. The [manufacturer specifications](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-laserjet-pro-4001dn/hp-laserjet-pro-4001dn-datasheet.pdf) allow for paper between 60 and 120 GSM, which roughly corresponds to between 16lb and 32lb bond paper. For higher quality reports, VotingWorks recommends paper on the thicker end of that scale such as HP Premium 32lb paper (PN: HPU1132) or equivalent. All report paper should be letter-sized. Using paper outside of the manufacturer specified weight range may result in jams and incorrect operation.

### Toner Specifications

The HP LaserJet Pro 4001dn requires genuine HP toner cartridges. Both the HP 148A Black Original LaserJet Toner Cartridge and the HP 148X High Yield Black Original LaserJet Toner Cartridge are acceptable.&#x20;

The printer is provided to customers initially with toner installed, which should last for many elections or even for the lifetime of the system. Low toner is indicated on the printer's small LED screen and also in the VxAdmin diagnostics section. When replacing the toner, refer to the [manufacturer's instructions](https://support.hp.com/us-en/document/ish_5455373-5578919-16).

### Diagnostics & Troubleshooting

VxAdmin features diagnostics for troubleshooting the printer. After authenticating and navigating to the **Diagnostics** menu, you can select **Print Test Page** to print a mock report. The diagnostics interface will also provide the printer status, including if paper is jammed or toner is low. For the most common issues, refer to the [hp-printer-faq](https://app.gitbook.com/s/JtZutzGTdCzsGITrdiph/vxadmin-system-setup/vxadmin-printer-faqs#hp-printer-faq "mention") in the user manual. For more other issues, refer directly to the [manufacturer user guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/hp-laserjet-pro-4001dn/hp-laserjet-pro-4001dn-user-guide.pdf).

## VxCentralScan Scanner Maintenance

VxCentralScan supports scanning with either the Ricoh fi-7600 or the Ricoh fi-8170.

### fi-7600 Large Desktop Scanner

The Ricoh fi-7600 [manufacturer specifications](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-7600/ricoh-fi-7600-datasheet.pdf) and [manufacturer operator's guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-7600/ricoh-fi-7600-user-guide.pdf) and included in the documentation repository.

The scanner must be periodically cleaned to ensure image quality, before every election and after every 10,000 sheets scanned within an election. If streaks are detected in an image while scanning, the software will proactively alert the user to clean the scanner. To clean the scanner, follow the cleaning instructions in the [manufacturer's consumable replacement and cleaning guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-7600/ricoh-fi-7600-cleaning-guide.pdf). VotingWorks recommends using Ricoh Cleaner F1 (PN: PA03950-0352) with cleaning wipes (PN: CG90000-120001) or equivalent.

The scanner's brake rollers (PN: PA03740-K010) and pick rollers (PA03740-K011) must be replaced every 250,000 sheets or every year, whichever is sooner. To replace these consumables, follow the instructions in the [manufacturer's consumable replacement and cleaning guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-7600/ricoh-fi-7600-cleaning-guide.pdf). In order to get all consumables and cleaning supplies together, you may choose to purchase the fi-7600 ScanAid kit (PN: CG01000-288701).

### fi-8170 Compact Desktop Scanner

The Ricoh fi-8170 [manufacturer specifications](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-8170/ricoh-fi-8170-datasheet.pdf) and [manufacturer operator's guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-8170/ricoh-fi-8170-datasheet.pdf) are included in the documentation repository.

The scanner must be periodically cleaned to ensure image quality, before every election and after every 5,000 sheets scanned within an election. If streaks are detected in an image while scanning, the software will proactively alert the user to clean the scanner. To clean the scanner, follow the cleaning instructions in the [manufacturer's consumable replacement and cleaning guide](https://github.com/votingworks/docs-vxsuite-v4/blob/main/hardware-assets/cots-documentation/central-system/ricoh-fi-8170/ricoh-fi-8170-cleaning-guide.pdf). VotingWorks recommends using Ricoh Cleaner F1 (PN: PA03950-0352) with cleaning wipes (PN: CG90000-120001) or equivalent.

The scanner's brake rollers (PN: PA03810-0001) and pick rollers (PA03640-0002) must be replaced every 200,000 sheets or every year, whichever is sooner. To replace these consumables, follow the instructions in the [manufacturer's consumable replacement and cleaning guide](../). In order to get all consumables and cleaning supplies together, you may choose to purchase the fi-8170 ScanAid kit (PN: CG01000-302801).

## Maintenance Support & Spare Recommendations

For VxAdmin, VotingWorks recommends keeping an extra toner cartridge and an extra ream of report paper on hand at all times. For VxCentralScan, VotingWorks recommends keeping scanner cleaning materials on hand at all times. Maintenance tasks can be performed by election managers or system administrators at the central location where VxAdmin and VxCentralScan are used.

