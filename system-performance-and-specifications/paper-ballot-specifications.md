# Paper Ballot Specifications

The following defines the minimal specifications for VxSuite paper stock. Ballot layout requirements are enumerated in [hand-marked-ballots.md](../system-overview/hand-marked-ballots.md "mention") and [machine-marked-ballots.md](../system-overview/machine-marked-ballots.md "mention") in the System Overview.

## Hand Marked Ballots

VxSuite supports a wide range of paper for hand-marked paper ballot style printing within the following supported specifications:

* **Width**: 8.5"
* **Length**: 11", 14", 17", 22"
* **Weight:** 105-177gsm
* **Coating:** uncoated
* **Opacity:** >90%
* **Color:** white or any pastel color >=70 brightness. Contrast ratio of printed black text is 21:1 for white paper and will exceed 10:1 on other paper colors of specified brightness.
* **Watermarking:** none
* **Ink:** typical oil-based or soy-based inks are appropriate for printing presses; typical laser toner or inkjet ink are appropriate for smaller printers & copiers.
* **Folding:** ballots should not be folded through bubbles.
* **Bleed-through:** bleed through should not be present when using recommend paper weight (105-177 gsm) and marking method (ball point pen).
* **Margins:** the paper margins listed below are required for proper timing mark interpretation and adequate space for VxCentralScan imprinting outside of the ballot selection area and timing marks:
  * Left/right: 5mm (0.19685 in)
  * Top/bottom: 12pt (0.16667 in)
* **Print Run Size:** defer to your print vendor's established best practices for quality assurance. In the absence of a vendor recommendation, we recommend that print runs are a consistent size between 500 to 1,000 sheets — consistency eases ballot accounting and the moderate size allows for semi-frequent quality checks.

## Ballot Marking Device Ballots

VxMark requires a specific type of thermal paper ballot stock as required by the VSAP BMD 150 component:

* **Manufacturer:** Mitsubishi
* **Model:** Thermoscript TF 1467
* **Width:** 8"
* **Length:** 13.25"
* **Corner Cut:** 16mm, 45° cut, top-right of thermal coated side

TF 1467 paper is only provided in one configuration on white paper with a weight of 140gsm, an opacity greater than 90%, and thermal coating on one side. VxMark expects the thermal side to be fully blank and therefore pre-printing attributes such as watermarking, ink, and margins are not applicable. Similarly, these ballots are only to be used with ballot marking devices and attributes specific to hand-marking such as folding and bleed-through are also not applicable. Printed text contrast ratio of blank ink on white paper is 21:1.
