# VVSG 2.0 Documentation Map

Which page answers each VVSG 2.0 requirement that obliges VotingWorks to
document something. Use it to place new material (see `STYLE.md`) and to see
what is thin. Not published: GitBook shows only pages in `SUMMARY.md`.

Built 2026-11-17 from the VVSG 2.0 text (February 10, 2021) and the TDP and
user manual as of that date. Coverage: **Full**, **Partial** (what's
missing in Notes), **None**. `um:` = the user manual repo; other paths are
this repo. "ext" = a file in `votingworks/docs-vxsuite-v4` linked from the
page, not checked.

Test labs treat the user manual as part of the TDP. Partial and None rows
are known: leave them unless a test lab raises one. **Accepted** marks a
row a lab has accepted as it is.

## Guideline 3.1 — System Documentation

The TDP's outline is Guideline 3.1: 3.1.1–3.1.4 here, 3.1.5–3.1.7 in the
user manual, which `SUMMARY.md` links as the operations, L&A and maintenance
manuals.

### 3.1.1 System Overview

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.1-A System overview documentation | README.md; system-overview/*-function.md, *-hardware.md, software-overview.md | Full | |
| 3.1.1-B Functional diagram | README.md (system diagram); software-overview.md; hardware pages; access-control.md | Full | |
| 3.1.1-C System description | README.md; function pages; software-overview.md; hardware pages; networking.md; CDF and format pages | Partial | Item 9 (directory listings in install order) none; COTS software lacks manufacturer |
| 3.1.1-D Identify software and firmware by origin | software-overview.md; hardware pages | Partial | No in-house / COTS / modified-COTS classification; firmware not identified |
| 3.1.1-E Traceability of procured software | software-overview.md "Traceability of Procured Software"; hash-checksum-verification-of-dependencies.md | Full | Practice described; no formal declaration; firmware not covered |

### 3.1.2 System Performance

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.2-A System performance documentation | system-limits/; maximum-tabulation-rate.md; supported-voting-variations-and-languages.md; safety-security-privacy-and-continuity-of-operation.md (item 4); paper-ballot-specifications.md | Partial | Item 3 (reliability, maintainability, availability, portability) none; item 5 (standards) scattered |
| 3.1.2-B Maximum tabulation rate | system-limits/maximum-tabulation-rate.md | Full | |
| 3.1.2-C Reliably detectable marks | reliably-detectable-marks.md; system-settings.md; ballot-interpretation.md | Full | Marginal marks are VVSG's ambiguous marks (see the term note in `STYLE.md`) |
| 3.1.2-D Processing capabilities | processing-capabilities.md → README.md, system-settings.md | Partial | Settings not classed as extension / bypassable / opt-in / opt-out |

### 3.1.3 System Security

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.3-A System security documentation | system-security-auditing-and-logging/ (whole section) | Full | |
| 3.1.3-B Access control implementation | access-control.md; user-roles.md; defense-in-depth-and-least-privilege.md; password-and-credential-policies.md; um:vxadmin-system-setup/programming-cards.md | Partial | Item 4: no single list of privileged accounts (vendor role, `vx-vendor`, root, `vx-services`, `vx-ui`) with purpose and how to disable |
| 3.1.3-C Physical security | physical-security.md; procedural-and-operational-security.md; um:miscellaneous/seal-recommendations.md | Full | |
| 3.1.3-D Audit procedures | audit-procedure/; um:after-election-night/post-election-audit-resources.md | Full | The UM page's "future software release" note may be stale |

### 3.1.4 Software Installation

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.4-A Software installation documentation | software-installation.md and children; software-overview.md | Partial | Installed software only as a dependency chart plus lock files |
| 3.1.4-B Software information | software-overview.md → vxsuite-build-system inventories; ext COTS report | Accepted | Per-item detail lives in the build system's inventories |
| 3.1.4-C Software location information | imaging.md; system-integrity.md; vxsuite-build-system inventories | Accepted | As 3.1.4-B |
| 3.1.4-D Election specific software identification | vxsuite-build-system inventories | Accepted | As 3.1.4-B |
| 3.1.4-E Installation software and hardware | build-machine-configuration/; preparing-usb-drives-for-imaging.md; imaging.md | Full | |
| 3.1.4-F Software installation procedures | trusted-build/; imaging-machines/ | Full | |
| 3.1.4-G Baseline image creation | trusted-build/README.md; secure-boot-signing.md | Full | |
| 3.1.4-H Programmed device configuration replication | imaging.md; verifying-the-image-installed-on-a-machine.md; signed-hash-validation.md; system-integrity.md | Full | |
| 3.1.4-I Software installation record creation | software-installation-record-creation.md | Full | |
| 3.1.4-J Procurement of voting system software | secure-boot-signing.md; verifying-the-image-installed-on-a-machine.md | Partial | Trusted repository implied, not stated |
| 3.1.4-K Open market procurement of COTS software | hash-checksum-verification-of-dependencies.md | Partial | Not stated as open-market |
| 3.1.4-L Erasable storage media preparation | preparing-usb-drives-for-imaging.md | Full | |
| 3.1.4-M Trusted storage media | preparing-usb-drives-for-imaging.md | Partial | Implied, not stated |

### 3.1.5 System Operations (user manual)

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.5-A System operations documentation | um: whole manual | Partial | Item 8: no table of key dates relative to the start of voting |
| 3.1.5-B Support training | um: whole manual | Partial | No training material |
| 3.1.5-C Functions and modes | um:README.md; um:l-and-a-overview.md; function pages | Partial | No single summary of modes in the UM |
| 3.1.5-D Roles | um:programming-cards.md; user-roles.md | Full | |
| 3.1.5-E Conditional actions | um: error message pages; safety-security-privacy-and-continuity-of-operation.md | Full | |
| 3.1.5-F References | — | None | No consolidated reference list |
| 3.1.5-G Operational environment | um:miscellaneous/operational-environment.md | Partial | Telecommunications (none, except VxAdmin's LAN) and facilities not stated |
| 3.1.5-H Readiness testing | um:logic-and-accuracy-pre-election-testing/; um: diagnostics pages | Full | |
| 3.1.5-I Features | um: device sections; um:election-night-guides/reports.md; vxadmin-results-exports/; cast-vote-records.md | Full | |
| 3.1.5-J Support | um:README.md | Partial | No release or upgrade procedure |
| 3.1.5-K Transportation and storage | um:operational-environment.md; um: packing-up pages; um:retaining-and-removing-election-files.md | Full | |

### 3.1.6 System Maintenance (user manual)

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.6-A, -B, -E, -P | um:system-maintenance/ | Full | |
| 3.1.6-C Maintenance viewpoint | system-overview/ | Full via TDP | |
| 3.1.6-D Equipment overview details | hardware and function pages | Partial | Memory handling and power conversion thin |
| 3.1.6-F Preventive maintenance procedures | um: device maintenance manuals; um:backup-and-restore.md | Partial | No personnel numbers per task |
| 3.1.6-G Troubleshooting procedure details | um: error message and FAQ pages | Partial | No upgrade coordination or personnel |
| 3.1.6-H Special equipment | um: maintenance manuals | Partial | No statement that none is needed |
| 3.1.6-I Parts and materials | um:supply-list.md; um:approved-parts-list.md | Full | |
| 3.1.6-J Approved parts list | um:approved-parts-list.md | Partial | No quantities or size/value columns |
| 3.1.6-K, -L Marking devices, approved manufacturers | um:approved-parts-list.md; um:supply-list.md | Full | Pen color conflict: black vs black or blue |
| 3.1.6-M, -N Ballot stock | paper-ballot-specifications.md; bubble and summary ballot pages | Full | |
| 3.1.6-O Printer paper specification | um:approved-parts-list.md; um: maintenance manuals; paper-ballot-specifications.md | Full | |
| 3.1.6-Q Maintenance support and spares | um: maintenance manuals; safety-security-privacy-and-continuity-of-operation.md | Partial | No spare-device or personnel counts; VxMark manual has no spares section |

### 3.1.7 Training (user manual)

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 3.1.7-A Training documentation | um:programming-cards.md; um:README.md | Partial | No training section in either repo |
| 3.1.7-B Personnel | um:programming-cards.md; um:maintenance-overview.md | Partial | Skill per role, not per function; no counts |
| 3.1.7-C User functions versus manufacturer functions | um:maintenance-overview.md; um:vxscan-maintenance-manual.md | Partial | Maintenance only; no full list of VotingWorks-only functions |
| 3.1.7-D Training requirements | um:programming-cards.md | Partial | Durations only |

## Documentation Requirements Outside 3.1

| Requirement | Page(s) | Coverage | Notes |
| --- | --- | --- | --- |
| 1.3-A Reporting of manufacturer-performed tests | README (1).md; ext test reports | Unchecked | Nine fields per test, in ext reports |
| 1.3-B Coverage of manufacturer-performed tests | — | None found | Probably outside these repos |
| 2.1.1-B Durability estimation | warranty-model.md | Partial | No component or consumable rows |
| 2.2-A User-centered design process | usability-and-accessibility.md | Partial | Thin on participants and on results driving design |
| 2.5-B Unsafe concurrency | README (1).md | Full | |
| 3.2-A, -B, -D, -E, -F, -H, -J, -O Setup inspection | um:logic-and-accuracy-pre-election-testing/setup-inspection.md; signed-hash-validation.md | Full | |
| 3.2-C Setup inspection record generation | um:setup-inspection.md | Partial | Only the readiness report |
| 3.2-G Maximum and minimum values of storage locations | — | None | |
| 3.2-I Backup power operational range | um:setup-inspection.md | Partial | No nominal range |
| 3.2-K Cabling connectivity inspection | um:setup-inspection.md | Partial | Implicit |
| 3.2-L, -M Communications status inspection | um:pre-election-adjudication-setup.md | Partial | No check that networking is absent or off |
| 3.2-N Consumables | um:setup-inspection.md; um:supply-list.md | Partial | Usage estimates for toner only |
| 3.2-P Calibration | um:setup-inspection.md; um:vxscan/scanner-management.md | Partial | No nominal ranges or inspection procedure |
| 3.2-Q Checklist of properties | um:setup-inspection.md | Partial | Unused interfaces; per-check risks |
| 3.3-A Event logging documentation | logging.md | Full | |
| 3.3-B, 4.1-F CDF usage | ballot-definition-cdf.md; cast-vote-records.md; cdf-err-export.md; logging.md | Full | |
| 3.3-C Bar and other codes | public-documents/ballot-qr-code-data-format.md; signed-hash-validation.md; vxmark-function.md | Full | Imprinted audit string not checked |
| 4.1-E Event code documentation | logging.md; ext logging documentation | Full | |
| 4.2-B Public documented manufacturer formats | public-documents/; election-package/; csv-exports.md | Full | |
| 5.1-F Accessibility documentation | um: accessibility settings pages; usability-and-accessibility.md; function pages | Partial | No recommended accessibility procedures |
| 7.2-O Inactivity alerts | vxmark-function.md; vxmarkscan-function.md (Voting Sessions) | Full | 5 minutes, then 45 seconds to respond |
| 7.2-P Floor space | — | None | No wheelchair clear-space guidance |
| 7.3-O Instructions for election workers | um: election day guides and checklists | Full | |
| 8.1-H Sanitized headphones | um: sanitizing headphones include | Full | |
| 8.3-A, 8.4-A Usability test reports | usability-and-accessibility.md; ext reports | Full | Report format unchecked |
| 9.1.1-A Software independence | software-overview.md | Full | |
| 9.1.3-C Voter reported errors | um:vxmark/voting-sessions.md | Partial | Only spoil and re-vote |
| 9.1.4-B, 9.2-A Audit procedure and support | audit-procedure/; um:post-election-audit-resources.md | Full | |
| 9.4-B Random numbers for audit | vxscan-unique-identifiers.md; cast-vote-records.md | Partial | Audit ID secret key's generator not stated |
| 11.4-B Separation of duties | user-roles.md; procedural-and-operational-security.md | Partial | No separation-of-duties guidance |
| 13.3-E Key management documentation | access-control.md; cryptography.md; system-integrity.md; vxscan-unique-identifiers.md | Partial | Scattered; no compromise, revocation or rotation |
| 14.1-A Risk assessment | risk-assessment.md; ext | Full | |
| 14.1-B Addressing and accepting risk | ext risk assessment | Unchecked | |
| 14.1-C Security architecture description | risk-assessment.md → security architecture pages | Full | |
| 14.1-D Procedural and operational security | procedural-and-operational-security.md; um:setup-inspection.md | Full | |
| 14.2-F Secure configuration and hardening | defense-in-depth-and-least-privilege.md; system-integrity.md | Accepted | No configuration surface ("no config"), so no named baseline |
| 14.2-J Vulnerability management | known-vulnerabilities.md | Full | Dependency monitoring thin |
| 14.3-A Supply chain risk management strategy | hardware-criticality-and-supplier-analysis.md | Partial | No compromise response; hardware only |
| 14.3-B Criticality analysis | hardware-criticality-and-supplier-analysis.md; hardware pages | Full | |
| 14.3-C Bill of materials | hardware pages; software-overview.md | Partial | Hardware only |
| 15.2-B Error handling documentation | um: error message pages; software-overview.md | Full | |
| 15.3-C Malware protection updates | system-integrity.md; logging.md | Partial | Rationale, no update procedure |
| 15.4-A Internal network architecture | networking.md; um:pre-election-adjudication-setup.md | Partial | No diagram or data flow |
| 15.4-B Secure network configuration | networking.md | Partial | Little guidance for officials |
| 15.4-C Disabled wireless | networking.md | Full | |

## Pages Outside These Requirements

Answer requirements outside the documentation set, or support several:
election-package/ (formats), bubble and summary ballot pages, cast vote
records and results exports, election-and-contest-type-variations.md,
ballot-interpretation.md, diagnostics.md, signed-hash-validation.md,
logging.md, known-vulnerabilities.md, risk-assessment.md,
hardware-criticality-and-supplier-analysis.md, the security architecture
pages, guidance-for-test-labs.md, usability-and-accessibility.md,
audio-visual-and-display-screen-settings.md, README (1).md (QA manual),
warranty-model.md, public-documents/.

Not in `SUMMARY.md`: `system-security-auditing-and-logging.md` (a stub) and
`.gitbook/includes/untitled.md` (empty).
