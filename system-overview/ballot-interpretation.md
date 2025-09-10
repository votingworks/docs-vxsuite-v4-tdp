# Ballot Interpretation

Ballot interpretation begins with the front and back images of the ballot transmitted from the scanner. Once the images are available to the application, it starts by trying to interpreting the ballot as a [hand marked ballot](hand-marked-ballots.md).

The interpreter first crops the image received from the scanner and converts the grayscale image from the ballot into binary images using [Otsu's method](https://en.wikipedia.org/wiki/Otsu's_method). Otsu's method computes a dynamic black and white threshold that allows the interpreter to filter out differences due to tinted paper or light streaking.

<div><figure><img src="../.gitbook/assets/streak-crossing-marks-grayscale.png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/streak-crossing-marks-grayscale_debug_vertical_streaks.png" alt=""><figcaption></figcaption></figure></div>

Before trying to make sense of the ballot, the interpreter checks the images for vertical streaks. Vertical streaks likely indicate some sort of smudge or debris in the scanner that could interfere with the ballot image. The interpreter looks for columns of black without gaps, excluding the edges of the ballot which may be black simply from the way the scanner creates images.

<div><figure><img src="../.gitbook/assets/33c22b9d-108e-454e-8010-0abea110472b-back_debug_vertical_streaks.png" alt=""><figcaption><p>Vertical streak detected</p></figcaption></figure> <figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_vertical_streaks.png" alt=""><figcaption><p>No vertical streak detected</p></figcaption></figure></div>

If a streak is detected, the interpreter exits and surfaces the error to the application which will alert the user.

The interpreter then identifies the timing mark grid. It searches for all vertical line segments around the edges of the ballot and joins adjacent line segments to form shapes. The shapes are filtered and scored according to how closely they resemble timing marks. The interpreter then looks for patterns of three timing marks resembling the corners of the grid. If the four corners cannot be identified, the interpreter exits. Once the corners are identified, the interpreter looks for the rest of the timing marks along the lines between the corners.

<figure><img src="../.gitbook/assets/452452815-c8912b9b-d3ac-4888-a386-b4fd57749306.png" alt="" width="375"><figcaption></figcaption></figure>

Before proceeding with interpretation, the interpreter calculates the distance between horizontal timing marks to verify the scale at which the ballot was printed. The expected distance is derived from the  specifications for [hand-marked-ballots.md](hand-marked-ballots.md "mention"). If the timing marks are too close together, the interpreter rejects the ballot — ballots must be printed at full scale to be interpreted safely.

The interpreter will then search the bottom left and top right corners of the image for a QR code. Since ballots have QR codes in the bottom left corner, the location of the QR code determines the correct orientation of the ballot and the interpreter can flip the image right-side up if necessary:

<div><figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_qr_code.png" alt="" width="375"><figcaption><p>QR code search</p></figcaption></figure> <figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_complete_timing_marks_after_orientation_correction.png" alt="" width="375"><figcaption><p>Correctly oriented ballot</p></figcaption></figure></div>

The QR code includes ballot metadata - precinct, ballot style, election hash, ballot mode - but no vote information (see [hand-marked-ballots.md](hand-marked-ballots.md "mention")). Up until now, the two sides of a ballot have been interpreted in parallel. At this point, the QR code metadata on the front and back are compared to ensure that they match to form a valid ballot. The ballot information from the QR code indicates which ballot layout from the election definition that the ballot conforms to, including the position of all the bubbles, contests, and write-in areas.

Now the interpreter inspects the locations of all ballot bubbles to see how filled they are. Note that bubbles are not necessarily aligned with timing marks because they can be defined in fractional grid coordinates. Each bubble is compared with a bubble template to distinguish voter marks from the bubble itself and is scored accordingly. In the images below, the orange score is the "match score", or the confidence that the bubble was found correctly. The greenish score is the "mark score", or the amount that the bubble's area is filled in. An empty bubble would receive a mark score of 0% or close to it–typically less than 1%.

<figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_scored_bubble_marks.png" alt="" width="375"><figcaption><p>Ballot bubble scores</p></figcaption></figure>

The bubble mark scores are later compared against the mark thresholds in the system settings to determine whether the voter made an indication that should be counted. The recommended default definite mark threshold is 7%. Setting too low of a threshold may result in stray marks or ballot folds to be considered as marks. Setting too high of a threshold may result in reasonable voter marks not being detected. While ballot instructions should recommend voters fully fill in the bubbles, at a threshold of 7% the system will detect most voter marks that pass through the bubble.

<div><figure><img src="../.gitbook/assets/validmarks (2).png" alt=""><figcaption><p>Valid Marks</p></figcaption></figure> <figure><img src="../.gitbook/assets/invalidmarksshort.jpg" alt=""><figcaption><p>Invalid Marks</p></figcaption></figure></div>

After bubbles are scored, the interpreter will then determine the location of the contest options relative to the grid. The write-in areas are defined in the election definition relative to the contest option areas. The write-in areas are then scored, similarly to the bubbles. This step only occurs in jurisdictions allowing unmarked (unbubbled) write-ins because otherwise a write-in is valid based only on the bubble. Write-in areas that cross the write-in area threshold set in the system settings will be shown in the write-in adjudication flow in VxAdmin. The system's default write-in area threshold is 5%.

<div><figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_contest_layouts.png" alt="" width="375"><figcaption><p>Identifying contest options</p></figcaption></figure> <figure><img src="../.gitbook/assets/0db947fd-eb05-4ccb-8c09-ad7aee2e6564-front_debug_scored_write_in_areas.png" alt="" width="375"><figcaption><p>Scoring write-in areas</p></figcaption></figure></div>

After all bubbles and write-in areas are scored, interpretation is complete and the images are saved to disk. The votes are inferred from the bubbles based on the mark thresholds and eventually exported to cast vote records.

If interpretation didn't work, one possibility is that the ballot is actually a [machine marked ballot](machine-marked-ballots.md), so the interpreter will then attempt to interpret the ballot as a machine marked ballot. Since votes are encoded into the QR code, the interpreter only has to find the QR code. It searches the entire document for a QR code. By searching the top and bottom half separately, it can infer the orientation of the ballot because machine marked ballots have QR codes in the top right.
