# TDP Style Guide

How to write and edit the VxSuite Technical Data Package. It applies to new
text and to any passage being edited; bring a passage up to this guide when
you change it, and leave untouched passages alone.

The TDP describes the system for certification test labs and election
officials reviewing it. It is not a user manual: it explains what the system
does and how, so a reviewer can understand and verify it.

**How this guide works.** Every rule has an ID (`TDP-301`) so a review can
cite it. IDs are permanent: a new rule takes the next free number in its
section, and a removed rule's ID is never reused. Each rule states one
thing; an exception is part of the rule. The Guidance section at the end
explains the reasons behind rules and covers judgment calls; it is advice,
not something to flag. Claude and GitBook's Agent both review against this
file, which is the only copy: after changing it, re-import it into the
GitBook site's style guide.

## Structure

- **TDP-101** Put new material on the page `VVSG-MAP.md` names for its
  requirement.
- **TDP-102** A change that adds, merges, moves or renames pages keeps every
  documentation requirement answered and every link working, and updates
  `VVSG-MAP.md`.
- **TDP-103** Don't rename a file only because its name no longer matches
  its page title (`hand-marked-ballots.md` is "Bubble Ballots").
- **TDP-104** One H1 per page, identical to the page's title in
  `SUMMARY.md`.
- **TDP-105** A content page opens with one sentence that defines its
  subject or states its scope: "VxScan is the system's precinct scanner into
  which voters cast their ballots directly."
- **TDP-106** Function pages keep this section order: Configuration
  (Polling Place Selection, Ballot Mode, Unconfiguring) → Polls Management →
  Voting Sessions or Scanning → Display Formats and Interaction Modes →
  Printer Management.
- **TDP-107** Hardware pages keep this section order: Overview → Internals →
  COTS Components → Discussion of Critical Components.
- **TDP-108** Text duplicated across parallel pages (VxMark and VxMarkScan,
  the printer sections) stays duplicated, so each page stands alone.
- **TDP-109** A change to one copy of duplicated text is made to every copy
  in the same change.

## Voice and Tone

- **TDP-201** Third person, with the product, a user role or VotingWorks as
  the subject: "VxScan can be unconfigured by an election manager or system
  administrator."
- **TDP-202** Not "we" or "our".
- **TDP-203** Procedures use the imperative.
- **TDP-204** No contractions.
- **TDP-205** No asides or casual phrasing ("That's ok", "heads up", "a
  pleasant chime").
- **TDP-206** State the mechanism, not an absolute: "Kiosk mode prevents
  access to the operating system by…", not "which is not possible".
- **TDP-207** "Guarantee", "impossible" and "unalterable" only for a claim a
  test lab can verify.

## Level of Detail

- **TDP-301** Describe behavior and anything a test lab can observe or
  verify.
- **TDP-302** Describe, at the level of concept, the mechanisms behind
  result integrity and security, even where users never see them: ballot
  interpretation, tabulation and adjudication, cast vote record handling,
  authentication and access control, cryptography, logging, software
  integrity (including how USB drives are handled), and networking. Describe
  them by what happens and in what order.
- **TDP-303** For networking, describe what connections are possible and how
  they are protected, not how features such as multi-station adjudication
  use them.
- **TDP-304** Don't name internals: database tables, packages, functions,
  variables. Exception: a name that is part of an interface (an election
  package file, a setting key, a log event ID, a CDF attribute, a file path
  on the machine).
- **TDP-305** Name a third-party component only when a standard the system
  claims depends on it (OpenSSL and its FIPS validation for cryptography) or
  it is security-sensitive in itself. Otherwise describe what it does ("a
  consistent copy of the database, taken while the application runs").
- **TDP-306** Don't state default values for system settings: name the
  setting and what it does.
- **TDP-307** State fixed behavior, which is not a default: "After
  configuration, VxScan is in test ballot mode."
- **TDP-308** State a value VotingWorks recommends as a recommendation, not a
  default: "The recommended definite mark threshold is 7%."
- **TDP-309** Keep user interface detail out unless the behavior can't be
  described without it.

## Terminology

- **TDP-401** Product names exactly as written, never abbreviated: VxAdmin,
  VxCentralScan, VxMark, VxMarkScan, VxPrint, VxScan, VxSuite.
- **TDP-402** Use the VxSuite mark terms: a **marginal mark** (below the
  definite mark threshold, flagged for adjudication) and an **invalid
  mark**.
- **TDP-403** Where a page answers a VVSG mark requirement, give the VVSG
  term in parentheses: VxSuite's marginal mark is VVSG's *ambiguous* mark,
  and VxSuite's invalid mark is VVSG's *marginal* mark.
- **TDP-404** Expand an abbreviation on its first use on each page, as
  "Term (ABBR)": "cast vote record (CVR)". Product names are never expanded.
- **TDP-405** Use these terms, not the alternatives:

| ID | Use | Not |
| --- | --- | --- |
| TDP-410 | bubble ballot | hand-marked ballot (except in file names) |
| TDP-411 | summary ballot | machine-marked ballot (except in file names) |
| TDP-412 | hand-marked | hand marked |
| TDP-413 | ballot-marking device (BMD) | ballot marking device |
| TDP-414 | test ballot mode, official ballot mode | test mode, official mode |
| TDP-415 | cast vote record (CVR) | cast-vote record |
| TDP-416 | ballot measure contest | yes-no contest |
| TDP-417 | system administrator card | system admin card |
| TDP-418 | Secure Boot, Ethernet, Wi-Fi | secure boot, ethernet, Wi-fi |
| TDP-419 | tamper-evident | tamper evident |
| TDP-420 | USB drive | USB (as a noun) |

## Numbers and Sentences

- **TDP-501** Thousands separators from 1,000: "10,000 ballots".
- **TDP-502** A space between a number and its unit: "5 mm", "200 GB",
  "105–177 gsm".
- **TDP-503** Inches as "in.": "8.5 in.".
- **TDP-504** An en dash for ranges: "105–177 gsm".
- **TDP-505** Present tense for what the system does.
- **TDP-506** "Will" only for a consequence: "the importing machine will
  refuse to import".
- **TDP-507** "Must" for a requirement.
- **TDP-508** "Should" only for a recommendation, never for what the system
  does: state expected results directly ("The command returns `root`.").
- **TDP-509** The Oxford comma: "VxAdmin, VxCentralScan, and VxPrint".
- **TDP-510** "e.g.," and "i.e.," with a comma.
- **TDP-511** An em dash without spaces in prose.
- **TDP-512** Introduce a list with a full sentence ending in a colon.

## Markup

- **TDP-601** Inline code for things typed or stored: setting keys, file
  names, paths, users, log event IDs, enum values, commands.
  "`precinctScanEnableWriteInImageReport` is true."
- **TDP-602** User interface, when it must appear: inline code for anything
  clickable.
- **TDP-603** Straight double quotes for other text on screen.
- **TDP-604** Menu paths joined with " > ".
- **TDP-605** Definition lists as "**Term:** definition", with the colon
  inside the bold.
- **TDP-606** Headings are Title Case noun phrases ("Polling Place
  Selection").
- **TDP-607** No skipped heading levels.
- **TDP-608** No bold in headings, and no bold paragraphs standing in for
  headings.
- **TDP-609** `{% hint style="info" %}` for notes and user manual
  references.
- **TDP-610** A `warning` hint only in the Software Installation
  procedures, directly before a step that erases data.
- **TDP-611** No other hint styles, and no "NOTE:" paragraphs.
- **TDP-612** User manual references end a functional section, in an info
  hint, linked by GitBook space mention:

  ```
  {% hint style="info" %}
  **User Manual Reference:** [Configure VxScan](https://app.gitbook.com/s/Blk9V7L3xSoGDrocz6MA/... "mention")
  {% endhint %}
  ```

- **TDP-613** Pipe tables, unless a cell needs a list or several
  paragraphs.
- **TDP-614** Never edit GitBook's `width` attributes on tables by hand.

## Links and Citations

- **TDP-701** Link a whole page by GitBook mention.
- **TDP-702** Link a section by a relative link with an anchor.
- **TDP-703** Links to source code are pinned to the release tag the TDP
  documents (currently `v4.1.1`), never `main`.
- **TDP-704** Links into `docs-vxsuite-v4` (datasheets, reports, risk
  assessment) stay on `main`.
- **TDP-705** Descriptive link text, not "here" or a bare URL.
- **TDP-706** Prose says "VxSuite" unless the version is the point.
- **TDP-707** Cite VVSG inline in parentheses with its version: "(VVSG 2.0
  7.3-H)".
- **TDP-708** Cite an item of a requirement as ".N" and a sub-item as
  ".N.x" ("VVSG 2.0 7.3-B.1", "8.1-A.2.b"), and a range with an en dash
  ("14.1-C.1–4").
- **TDP-709** Cite only IDs that exist in VVSG 2.0, not test assertion IDs.
- **TDP-710** Cite NIST publications as "NIST SP 800-161".

## Figures

- **TDP-801** Figures for outputs a reviewer needs to see (printed reports,
  ballots, export structures), diagrams and hardware photos.
- **TDP-802** No step-by-step screenshots.
- **TDP-803** No highlights on screenshots.
- **TDP-804** A user interface screenshot only when the behavior can't be
  described without it.
- **TDP-805** GitBook figure markup, never Markdown images:

  ```
  <figure><img src="../.gitbook/assets/<name>.png" alt="<what it shows>" width="375"><figcaption><p>Sentence case caption</p></figcaption></figure>
  ```

- **TDP-806** Every figure has alt text.
- **TDP-807** Captions are in sentence case. A caption is optional when the
  text around the figure says what it shows.
- **TDP-808** Width 375 for screenshots and printed reports.
- **TDP-809** Width 563 for diagrams and wide tables.
- **TDP-810** Full width only for system diagrams.
- **TDP-811** A screenshot's file name is its gallery ID
  (`vxadmin-….png`).
- **TDP-812** Other new images get descriptive kebab-case names with no
  spaces.
- **TDP-813** Diagrams are SVG, named `diagram-<name>.svg`.
- **TDP-814** Diagram labels stay `<text>`, never outlined.
- **TDP-815** Diagram labels are set as `font-family: "Inter", sans-serif`.
- **TDP-816** Don't embed fonts in diagrams.
- **TDP-817** Diagram connector lines run unbroken under their labels;
  never cut a gap into a line for a label.
- **TDP-818** Each diagram label is drawn after the lines with a white halo,
  from a `.halo` class in the file's `<style>`.
- **TDP-819** Diagrams have a plain white background.

## Procedures

- **TDP-901** Numbered steps, one action each, in the imperative, often led
  by a purpose clause: "To clone the offline VM, run the following command
  on the build machine:".
- **TDP-902** Each command in full, in a fenced block after a step ending
  in a colon.
- **TDP-903** Define each `<placeholder>` value once.
- **TDP-904** State the expected result after a key step.
- **TDP-905** Notes inside a step are indented under it.

## Guidance

Advice and reasons, not rules to flag.

- **The outline is VVSG 2.0 Guideline 3.1:** System Overview (3.1.1),
  System Performance & Specifications (3.1.2), System Security, Auditing &
  Logging (3.1.3) and Software Installation (3.1.4). Operations,
  maintenance and training (3.1.5–3.1.7) are in the user manual, which test
  labs treat as part of the TDP. Many page titles are requirement titles
  ("Maximum Tabulation Rate" is 3.1.2-B), and a short page may exist only to
  answer one. `VVSG-MAP.md` maps every documentation requirement to the page
  that answers it; check any change to the page structure against it.
- **Most changes edit existing pages.** A reorganization can be proposed
  when it is well motivated (TDP-102).
- **Renaming a file only to match its title** (TDP-103) breaks links for no
  reader-visible gain.
- **Too deep?** If a refactor that changes no behavior would make a
  sentence false, it names internals (TDP-304).
- **Defaults vary by state,** which is why the TDP names settings without
  their default values (TDP-306).
- **Pinned links** (TDP-703) move to a new release tag all together.
  `docs-vxsuite-v4` stays on `main` because that repository has no release
  tags.
- **Screenshots come from the gallery.** The screenshots workflow keeps
  files named by gallery ID current (TDP-811). The user manual has the
  step-by-step screenshots (TDP-802).
- **Diagrams are edited as text,** so renaming a label is a text edit only.
  GitBook strips embedded fonts (TDP-816), so readers see their own
  sans-serif unless they have Inter. GitBook also strips `paint-order` as an
  attribute, which is why the halo is a class (TDP-818), and the halo needs
  the white background (TDP-819). A new diagram can start from a Figma SVG
  export with "Outline text" off; the file in this repo is then its source.
- **Don't delete images in a docs pull request,** even ones a change stops
  using. Deleting any image makes GitBook rebuild the whole space, so its
  diff marks every page as edited. An unused image is harmless; remove
  unused images in a separate cleanup pull request.
