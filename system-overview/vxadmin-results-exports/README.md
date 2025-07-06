# VxAdmin Results Exports

VxAdmin supports a variety of results exports.&#x20;

[Tally reports](tally-reports.md) contain contest results for the full election or a specific subset of ballots. They can be printed directly from VxAdmin, exported as PDFs, or exported in [CSV format](csv-exports.md#tally-report-csv-structure). In addition, full election results can be exported as an [Election Results Reporting CDF](cdf-err-export.md) JSON file.

[Ballot count reports ](ballot-count-reports.md)include only ballot counts, without contest results. They can also be printed directly from VxAdmin, exported as PDFs, or exported in [CSV format](csv-exports.md#ballot-count-report-csv-structure).

The [write-in adjudication report](write-in-adjudication-report.md) acts as a summary of all write-in adjudication activity or as a "scatter report." The tally reports consolidates write-in candidates whose vote totals are too small to affect the contest outcomes. The counts for those write-in candidates are available in the write-in adjudication report. The write-in adjudication report may be printed directly from VxAdmin or exported as a PDF.

For all VxAdmin reports, the report is either "Official" or "Unofficial." If the report is exported before the results are marked as official in the application, the results are "Unofficial." If the report is exported after the results are marked as official in the application, the results are "Official." All visual reports have "Official" or "Unofficial" included in the title and all exported files will have "official" or "unofficial" included in the filename.
