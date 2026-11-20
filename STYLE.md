# TDP Style Guide

How to write and edit the VxSuite Technical Data Package. It applies to new
text and to any passage being edited; bring a passage up to this guide when you
change it, and leave untouched passages alone. The user manual has its own
guide.

The TDP describes the system for certification test labs and election
officials reviewing it. It is not a user manual: it explains what the system
does and how, so a reviewer can understand and verify it.

## Structure

- The TDP's outline is VVSG 2.0 Guideline 3.1: System Overview (3.1.1),
  System Performance & Specifications (3.1.2), System Security, Auditing &
  Logging (3.1.3) and Software Installation (3.1.4). Operations, maintenance
  and training (3.1.5–3.1.7) are in the user manual, which test labs treat
  as part of the TDP. Many page titles are requirement titles ("Maximum
  Tabulation Rate" is 3.1.2-B), and a short page may exist only to answer
  one. `VVSG-MAP.md` maps every documentation requirement to the page that
  answers it. Check any change to the page structure against it.
- Most changes edit existing pages: put new material on the page
  `VVSG-MAP.md` names for its requirement. A reorganization (adding, merging,
  moving or renaming pages) can be proposed when it is well motivated; it
  must keep every requirement answered and every link working, and update
  `VVSG-MAP.md`.
- A file name that no longer matches its page title is fine
  (`hand-marked-ballots.md` is "Bubble Ballots"); renaming a file only for
  that breaks links for no reader-visible gain.
- One H1 per page, identical to the page's title in `SUMMARY.md`.
- A content page opens with one sentence that defines its subject or states
  its scope: "VxScan is the system's precinct scanner into which voters cast
  their ballots directly."
- Function pages keep one section order: Configuration (Polling Place
  Selection, Ballot Mode, Unconfiguring) → Polls Management → Voting Sessions
  or Scanning → Display Formats and Interaction Modes → Printer Management.
  Hardware pages: Overview → Internals → COTS Components → Discussion of
  Critical Components.
- Text duplicated across parallel pages (VxMark and VxMarkScan, the printer
  sections) stays duplicated so each page stands alone. A change to one copy
  is made to every copy in the same change.

## Voice and Tone

- Third person, with the product, a user role or VotingWorks as the subject:
  "VxScan can be unconfigured by an election manager or system administrator."
  Not "we" or "our". Procedures use the imperative.
- Plain and neutral. No contractions, asides or casual phrasing ("That's ok",
  "heads up", "a pleasant chime").
- State the mechanism, not an absolute. Write "Kiosk mode prevents access to
  the operating system by…", not "which is not possible". Use "guarantee",
  "impossible" or "unalterable" only for a claim a test lab can verify.

## Level of Detail

- Describe behavior and anything a test lab can observe or verify.
- Also describe, at the level of concept, the mechanisms behind result
  integrity and security, even where users never see them: ballot
  interpretation, tabulation and adjudication, cast vote record handling,
  authentication and access control, cryptography, logging, software
  integrity (including how USB drives are handled), and networking (what
  connections are possible and how they are protected, not how features
  such as multi-station adjudication use them). Describe them by what
  happens and in what order.
- Do not name internals: database tables, packages, functions, variables. A
  name that is part of an interface is fine: an election package file, a
  setting key, a log event ID, a CDF attribute, a file path on the machine.
  Test: if a refactor that changes no behavior would make the sentence false,
  it is too deep.
- Name a third-party component only when a standard the system claims
  depends on it (OpenSSL and its FIPS validation for cryptography) or it is
  security-sensitive in itself. Otherwise describe what it does ("a
  consistent copy of the database, taken while the application runs").
- Do not state default values for system settings; they vary by state. Name
  the setting and what it does. Fixed behavior is not a default and is
  stated ("After configuration, VxScan is in test ballot mode"). A value
  VotingWorks recommends is stated as a recommendation, not a default ("The
  recommended definite mark threshold is 7%").
- Keep user interface detail out unless the behavior can't be described
  without it.

## Terminology

Product names exactly as written: VxAdmin, VxCentralScan, VxMark, VxMarkScan,
VxPrint, VxScan, VxSuite. Use these terms, not the alternatives:

| Use | Not |
| --- | --- |
| bubble ballot | hand-marked ballot (except in file names) |
| summary ballot | machine-marked ballot (except in file names) |
| hand-marked | hand marked |
| ballot-marking device (BMD) | ballot marking device |
| test ballot mode, official ballot mode | test mode, official mode |
| cast vote record (CVR) | cast-vote record |
| ballot measure contest | yes-no contest |
| system administrator card | system admin card |
| Secure Boot, Ethernet, Wi-Fi | secure boot, ethernet, Wi-fi |
| tamper-evident | tamper evident |
| USB drive | USB (as a noun) |

Mark terms differ from VVSG 2.0's: a VxSuite **marginal mark** (below the
definite mark threshold, flagged for adjudication) is what VVSG calls an
*ambiguous* mark, and a VxSuite **invalid mark** is what VVSG calls a
*marginal* mark. Use the VxSuite terms, and give the VVSG term in
parentheses where a page answers a VVSG mark requirement.

Expand an abbreviation on its first use on each page, as "Term (ABBR)", e.g.,
"cast vote record (CVR)". Product names are never expanded.

## Numbers and Units

- Thousands separators from 1,000: "10,000 ballots".
- A space between a number and its unit: "5 mm", "200 GB", "105–177 gsm".
- Inches as "in.": "8.5 in.".
- An en dash for ranges: "105–177 gsm".

## Sentences

- Present tense for what the system does; "will" only for a consequence:
  "the importing machine will refuse to import".
- "Must" for a requirement, "should" for a recommendation. Not "should" for
  what the system does; state expected results directly: "The command returns
  `root`."
- The Oxford comma: "VxAdmin, VxCentralScan, and VxPrint".
- "e.g.," and "i.e.," with a comma. An em dash without spaces in prose.
- Introduce a list with a full sentence ending in a colon.

## Markup

**Inline code** for things typed or stored: setting keys, file names, paths,
users, log event IDs, enum values, commands. `precinctScanEnableWriteInImageReport`
is true.

**User interface**, when it must appear: inline code for anything clickable,
straight double quotes for other text on screen. Menu paths joined with
" > ".

**Definition lists**: "**Term:** definition", the colon inside the bold.

**Headings**: Title Case noun phrases ("Polling Place Selection"). No skipped
levels, no bold headings, no bold paragraphs standing in for headings.

**Hints**: `{% hint style="info" %}` for notes and user manual references.
A `warning` hint only in the Software Installation procedures, directly
before a step that erases data. No other hint styles, and no "NOTE:"
paragraphs.

**User manual references** end a functional section, in an info hint, linked
by the GitBook space mention:

```
{% hint style="info" %}
**User Manual Reference:** [Configure VxScan](https://app.gitbook.com/s/vh0Xx7zclRU0SsZ9mvKy/... "mention")
{% endhint %}
```

**Tables**: pipe tables, unless a cell needs a list or several paragraphs.
Never edit GitBook's `width` attributes by hand.

**Links**:
- Whole pages by GitBook mention links; sections by relative links with an
  anchor.
- Source code pinned to the release tag the TDP documents (currently
  `v4.1.1`), never `main`. Links into `docs-vxsuite-v4` (datasheets,
  reports, risk assessment) stay on `main`: that repository has no release
  tags.
- Descriptive link text, not "here" or a bare URL.
- Prose says "VxSuite" unless the version is the point.

**Standards**: cite VVSG inline in parentheses with its version, "(VVSG 2.0
7.3-H)"; an item of a requirement as ".N", a sub-item as ".N.x" ("VVSG 2.0
7.3-B.1", "8.1-A.2.b"), a range with an en dash ("14.1-C.1–4"). Cite only
IDs that exist in VVSG 2.0, not test assertion IDs. NIST publications as
"NIST SP 800-161".

**What gets a figure**: outputs a reviewer needs to see (printed reports,
ballots, export structures), diagrams and hardware photos. No step-by-step
screenshots (the user manual has those) and no highlights; a user interface
screenshot only when the behavior can't be described without it.

**Figures**: GitBook figure markup, never Markdown images:

```
<figure><img src="../.gitbook/assets/<name>.png" alt="<what it shows>" width="375"><figcaption><p>Sentence case caption</p></figcaption></figure>
```

- Alt text is required. A caption is optional when the text around the
  figure says what it shows; captions are in sentence case.
- Width 375 for screenshots and printed reports, 563 for diagrams and wide
  tables, full width only for system diagrams.
- Screenshots use their gallery ID as the file name (`vxadmin-….png`); the
  screenshots workflow keeps them current. Other new images get descriptive
  kebab-case names with no spaces.
- Diagrams are SVG (`diagram-<name>.svg`), edited as text: labels stay
  `<text>` (never outlined), and each file embeds the Inter font it uses so
  it renders the same in GitBook. A new diagram can start from a Figma SVG
  export with "Outline text" off; the file in this repo is then its source.

## Procedures

- Numbered steps, one action each, in the imperative, often led by a purpose
  clause: "To clone the offline VM, run the following command on the build
  machine:".
- Show each command in full in a fenced block after a step ending in a colon.
  Define `<placeholder>` values once.
- State the expected result after a key step.
- Notes inside a step are indented under it.
