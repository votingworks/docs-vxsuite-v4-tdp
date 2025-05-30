---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Hand Marked Ballots

VxSuite can tabulate a wide variety of ballot designs as long as they conform to the following requirements:

1. Ballot size must be one of the available system options
2. Ballot must include correctly formatted timing mark borders
3. Ballot must include an appropriately positioned metadata QR code
4. Ballot must use a specific bubble shape
5. Ballot must adhere to [system limits](../system-performance-and-specifications/system-limits/#hand-marked-paper-ballots)

## Ballot Size

There are six valid ballot sizes. All are 8.5 inches in width, but vary in height:

| Name       | Length | Width |
| ---------- | ------ | ----- |
| Letter     | 11"    | 8.5"  |
| Legal      | 14"    | 8.5"  |
| Custom 17" | 17"    | 8.5"  |
| Custom 22" | 22"    | 8.5"  |

These lengths correspond to the length specified in the [Ballot Layout](hand-marked-ballots.md) within the election definition.

## Timing Mark Borders

<figure><img src="../.gitbook/assets/image (21).png" alt="" width="563"><figcaption><p>Example of timing mark borders on letter-sized paper (scaled)</p></figcaption></figure>

Every ballot must have timing mark borders on both front and back. The timing marks and page margins are strictly defined:

| Dimension                 |                |
| ------------------------- | -------------- |
| Timing Mark Width         | 3/16 in.       |
| Timing Mark Height        | 1/16 in.       |
| Page Margin (Top, Bottom) | 12pt (1/6 in.) |
| Page Margin (Left, Right) | 5mm            |

As for number of timing marks, there are always 34 in the top and bottom borders, which has a 32 x 39 grid of possible bubble positions inside the timing mark border. The number of marks in the left and right borders varies based on the length of the ballot, and should be calculated by the formula **(# inches \* 4) - 3**. For example, a letter-sized ballot (11 inches) should have 41 left and right timing marks whereas a legal-sized ballot (14 inches) should have 53 left and right timing marks.

The timing marks must be aligned to the margins of the page and evenly spaced.

## QR Code Metadata

The ballot must include a QR code which contains key metadata about the ballot.

### QR Code Content

The QR code includes ballot metadata:

* Precinct Index - corresponds to a precinct in the election definition
* Ballot Style Index - corresponds to a ballot style in the election definition
* Page Number - page number within the ballot style
* Test Ballot Flag - indicates whether the ballot is a test ballot or an official ballot
* Ballot Type (Precinct, Absentee, or Provisional)

In addition, the QR code includes the [ballot hash](election-package/#ballot-hash-and-election-package-hash). The ballot hash ensures that the ballot was generated from the same election definition that will be used to interpret the ballot.

For full specifications on how to generate readable QR codes, refer to the [ballot-qr-code-data-format.md](../public-documents/ballot-qr-code-data-format.md "mention").

### Metadata QR Code Placement

The interpreter looks for the QR code in the bottom-left corner of the ballot. The detection area is a square whose sides are 1/4 of the ballot width.&#x20;

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption><p>The highlighted area must contain the metadata QR code</p></figcaption></figure>

## Bubble Format

In order to be interpreted correctly, bubbles must meet the following dimensions:

| Dimension      | Measurement   |
| -------------- | ------------- |
| Width          | 0.20"         |
| Height         | 0.13"         |
| Border Radius  | 0.7"          |
| Line Thickness | 1px (0.265mm) |

<figure><img src="../.gitbook/assets/Screen Shot 2024-09-26 at 11.59.35 AM.png" alt="" width="563"><figcaption><p>Bubble example (not to scale)</p></figcaption></figure>

## Grid Coordinates

The timing mark borders define an abstract grid that VxSuite uses to assign coordinates to positions on the ballot. In the election definition, bubble positions and other ballot regions are specified using these grid coordinates. The ballot grid is an XY grid with the origin in the top-left corner. For example, the coordinate **(5, 3)** would correspond to the following position on the ballot:

<figure><img src="../.gitbook/assets/image (27).png" alt="" width="563"><figcaption></figcaption></figure>

**Notes:**

* Coordinates correspond to the _center_ of each timing mark
* Coordinates specify the _center_ of each bubble
* Fractional coordinates are allowed

## Complete Example

Below is a complete ballot that, when paired with the appropriate election definition, could be interpreted within VxSuite:

<figure><img src="../.gitbook/assets/image (28).png" alt="" width="563"><figcaption><p>Valid ballot with timing marks, QR code, and bubbles</p></figcaption></figure>
