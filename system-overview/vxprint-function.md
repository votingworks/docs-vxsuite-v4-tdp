# VxPrint Function

VxPrint is the system's on-demand ballot printer. It prints blank official and test ballots for voters at the polling place, using the pre-rendered ballots included in the election package. VxPrint is not a marking device or a tabulator — voters mark the ballots it prints by hand, and those ballots are later cast and tabulated at VxScan or VxCentralScan.

## Configuration

VxPrint is configured with a signed [election-package](election-package/ "mention") exported from VxAdmin, loaded by an election manager from a USB drive. In addition to the election definition and system settings, the election package must contain the [ballots file](election-package/#ballots), which holds the pre-rendered ballot PDFs that VxPrint prints. If the election package does not include any ballots, configuration will fail and VxPrint will surface an error to the user.

{% hint style="info" %}
User Manual Reference: \[INSERT LINK]
{% endhint %}

### Polling Place Selection

The election manager can choose to select a polling place for the device. The selected polling place determines which precincts, splits, and ballot styles are available to print for poll worker users. If the election manager makes no choice of polling place, poll workers will be able to print any ballot style. Election managers are always able to print any ballot style.

### Ballot Mode

The election manager can toggle between official ballot mode and test ballot mode. In official ballot mode, the ballots printed at VxPrint are official ballots; in test ballot mode, they are test ballots. Switching between ballot modes clears the count of printed ballots. After configuration, VxPrint is in official ballot mode by default.&#x20;

### Unconfiguring

VxPrint can be unconfigured by an election manager or system administrator.

## Printing Ballots

Once VxPrint is configured, an election manager or poll worker can print ballots. The operator selects the attributes of the ballot to print:

* **Precinct** — and the **split**, if the precinct is divided into splits
* **Party** — for closed primary elections only
* **Language** — for multilingual elections only
* **Ballot type** — precinct or absentee (election managers only)
* **Number of copies** (election managers only)

VxPrint then prints the requested ballot(s) on the connected COTS printer. It records a running count of how many ballots have been printed, broken down by these attributes, for the current ballot mode.&#x20;

The supported printer is the HP LaserJet Pro 4001dn. VxPrint must be connected to a printer before it can print.

{% hint style="info" %}
User Manual Reference: \[INSERT LINK]
{% endhint %}

## Ballots Printed Report

VxPrint can produce a ballots printed report summarizing how many ballots have been printed, grouped by precinct, split, party, and language, with separate counts for precinct and absentee ballots. The report can be printed directly or exported to a USB drive as a PDF.

{% hint style="info" %}
User Manual Reference: \[INSERT LINK]
{% endhint %}

## Printer Management

The supported printer is the HP LaserJet Pro 4001dn.&#x20;

VxPrint interfaces with the printer through CUPS, the open-source printing system developed by Apple and installed on our Debian system. When a printer is attached, it is registered with the CUPS server and made available to the application. VxPrint is able to send print jobs to the printer via CUPS commands. The HP LaserJet Pro does not require any additional third-party or in-house driver because it supports the IPP (Internet Printing Protocol) which CUPS then utilizes.

Using IPP, VxPrint is also able to poll the detailed status (toner level, jam status, etc.) of the printer for use in the diagnostics interface.

VxPrint can only connect with one printer at a time and will always connect with the first attached printer.
