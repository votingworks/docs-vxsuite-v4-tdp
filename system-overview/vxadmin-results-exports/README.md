---
layout:
  width: default
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
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# VxAdmin Results Exports

VxAdmin supports a variety of results exports.&#x20;

[Tally reports](tally-reports.md) contain contest results for the full election or a specific subset of ballots. They can be printed directly from VxAdmin, exported as PDFs, or exported in [CSV format](csv-exports.md#tally-report-csv-structure). In addition, full election results can be exported as an [Election Results Reporting CDF](cdf-err-export.md) JSON file.

[Ballot count reports ](ballot-count-reports.md)include only ballot counts, without contest results. They can also be printed directly from VxAdmin, exported as PDFs, or exported in [CSV format](csv-exports.md#ballot-count-report-csv-structure).

The [write-in reports](write-in-adjudication-report.md) cover write-in adjudication activity: the write-in adjudication report summarizes all write-in adjudication, including the counts for write-in candidates that tally reports consolidate when their vote totals are too small to affect contest outcomes, while the write-in image report shows the write-in images for a contest grouped by candidate. Both may be printed directly from VxAdmin or exported as PDFs.

The [voter turnout report](voter-turnout-report.md) shows turnout by precinct, comparing ballots cast against the registered voter counts included in the election package.

For all VxAdmin reports, the report is either "Official" or "Unofficial." If the report is exported before the results are marked as official in the application, the results are "Unofficial." If the report is exported after the results are marked as official in the application, the results are "Official." All visual reports have "Official" or "Unofficial" included in the title and all exported files will have "official" or "unofficial" included in the filename.
