# Quality Assurance Manual

VxSuite product quality is ensured through both focused processes on individual aspects of the system and through overall integration testing that ensure the system is working well end-to-end.

## Quality Assurance Protocols – Software

### Automated Unit Tests

VotingWorks code has extensive unit test coverage. All libraries in the [vxsuite repository](https://github.com/votingworks/vxsuite/tree/v4.0.0-release-branch) have near 100% coverage, meaning that almost every single line of code runs whenever testing is run. Across all libraries, there are over 3,000 unit tests which all together include over 10,000 assertions about the software's behavior.

Each test always either passes or fails. A test fails if an error is thrown or an assertion fails. An assertion may be something like "the phrase _General Election_ appear on screen" or "there are 56 votes for a specific candidate after loading cast vote records."&#x20;

Whenever changes are made to VotingWorks code, all tests are automatically run as part of a continuous integration (CI) process through CircleCI. Code changes cannot be merged unless all tests pass. A single failing test will prevent changes from being merged. Every test run on CirceCI provides evidence that the software is operating as expected.

Test runs are public information available via CircleCI. For example, tests running in `vxsuite` are tracked [here](https://app.circleci.com/pipelines/github/votingworks/vxsuite).

If tests are flaky, meaning that they usually pass but occasionally don't, VotingWorks investigates and fixes the underlying issue. Flaky tests are automatically reported by the CircleCI tooling. VotingWorks reviews new flaky tests on a weekly basis.

### Automated End-to-End Tests

In addition to unit tests, VotingWorks code has end-to-end integration tests for all applications. These operate in the same continuous integration framework as the unit tests, but ensure the system works at higher-level. Instead of simply running the application server or the frontend, the entire stack is simulated to ensure that the components of the system - data store, user interface, communication between processes - are working as expected. Like unit tests, these tests are run before any code change is merged.

### Regression Testing

Whenever a software issue is discovered in manual testing or in actual operation in the field, VotingWorks creates an automated regression test after fixing the issue. For example if a particular ballot image was not interpreted but should have been interpreted, that ballot image would be used to create an automated regression test to ensure that not only is the issue fixed but that future changes cannot recreate the issue.

Even tests which are not explicitly created as regression tests have an anti-regression function. The advantage of having a robust test suite is that failing tests will inform developers when new fixes or improvements break previous functionality.

### Manual Testing

While we strive to cover as much as we possibly can with automated tests, there remains significant value in rigorous manual testing of software on actual hardware. We periodically conduct such passes and perform particularly rigorous passes before freezing software for a release.

To organize this process, we make use of checklists. A base set of checklists can be viewed here: [Software QA Checklists](https://github.com/votingworks/docs-vxsuite-v4/blob/main/quality-assurance/Software%20QA%20Checklists.pdf). When performing QA before a release for a particular state or election, we often tweak these base checklists to hone in on the specific circumstances, e.g., using specific adjudication settings and paper ballot lengths.

### Safe Concurrency (2.5-B)

VxSuite practices safe concurrency by using programming languages that, in their design, avoid the most common dangers of concurrency.&#x20;

Most of the application code, both frontend and backend, is written in TypeScript which compiles to JavaScript executing at runtime. JavaScript is a single-threaded language. While code can execute asynchronously, it cannot execute simultaneously with other code, preventing most instances of unsafe concurrency. We do sometimes make use of a mutex, and our TypeScript mutex implementation is [well-tested](https://github.com/votingworks/vxsuite/blob/v4.0.0-release-branch/libs/utils/src/mutex.test.ts).

Performance-critical parts of the application, like image processing for ballot interpretation, are written in [Rust](https://www.rust-lang.org/). Rust was designed specifically to be a memory-safe language alternative to common low-level alternatives like C. It requires that every piece of memory has a single owner responsible for the memory's lifecycle. Unsafe memory operations are prevented by the tooling itself - the compiler and linter - to ensure memory-safe programs. The language is recommended for security critical operations by the White House ([2024 Report](https://www.whitehouse.gov/wp-content/uploads/2024/02/Final-ONCD-Technical-Report.pdf)) and industry leaders. While memory safety and concurrency safety are slightly different things, the two are deeply intertwined, and a memory-safe language avoids most of the pitfalls of unsafe concurrency.

Despite those protections, unsafe concurrency is technically still possible, as it is widely acknowledged as impossible to definitively prove that a complex piece of software is free of race conditions.

In order to catch any other instances of unsafe concurrency, VotingWorks tests software operation at scale in automated tests, as discussed above. In actively developed repositories like those for VxSuite, tests are running hundreds or thousands of times before the software is actually used on a machine. At that scale, intermittent concurrency issues are surfaced in the form of flaky tests. VotingWorks reviews flaky tests weekly and uses them to identify and fix any concurrency issues.

Once software is actually imaged to hardware, VotingWorks tests the software thoroughly and at high volumes. For example on VxScan, the `precinctScanEnableShoeshineMode` flag in the [#system-settings](system-overview/election-package/#system-settings "mention") allows testing the scanner with a repeated scan that is run thousands of times before a release. In addition, VotingWorks attempts to identify edge cases and break the software during testing by performing operations in unusual or rapid succession which may reveal concurrency issues.

## Quality Assurance Protocols – Hardware

### Hardware Design

VotingWorks uses large-scale COTS hardware wherever possible, including laptops, single-board computers, document scanners, and printers. By virtue of designing around components that are produced and field-tested at much higher scale than voting machines ever can be, we reduce the chance of a quality problem at the design phase.

For components that must be custom-made, for example the VxScan precinct scanner module and the ballot box, we have followed the industry-standard multi-phase design process to ensure that quality issues are caught early, long before we've committed to large production runs. In particular:

* **design prototyping** – every individual hardware component is prototyped using 3D-printing and laser-cut parts in order to validate CAD designs, in particular when managing a paper path.
* **lab prototypes** – every hardware subsystem – e.g. the VxScan module or the VxBox ballot box – goes through multiple lab prototypes of increasing fidelity. Each prototype is fully functional and is tested with thousands of ballots, through setup and teardown repeatedly. Weaknesses are cataloged and fed into the next lab prototype.
* **engineering prototype** – once the lab prototype is fully validated, an engineering prototype is designed, tweaked for manufacturing (DFM). The tooling is then built, in order to produce an engineering prototype that is as close as possible to the final product. The tooling is adjusted in minor ways based on tests performed on the engineering prototype.

By the time a VotingWorks hardware subsystem goes to assembly-line production, it has gone through a number of iterations to ensure that the design is high quality. &#x20;

### Component Testing & Validation

VotingWorks works closely with suppliers to ensure quality components. We require suppliers to provide documentation of their QA procedures (TA2.1.1-A.2 1). VotingWorks's policy is to report all defective components to the supplier in order to jointly plan mitigations for future orders.

VotingWorks component test procedures vary on a component-by-component basis:

* **Custom Manufactured Parts** - Metal and plastic parts manufactured specifically for VotingWorks (e.g. a metal panel in VxScan) are visually inspected and measured against dimensions specifified in their engineering drawings.
* **Complex Electrical Subassemblies** - Large electrical components, which are often critical components, are tested before being installed in any machine. For example, the embedded scanner in VxScan is tested for motor control and image quality. VotingWorks has command-line interfaces that allow controlling and testing devices outside of a full software installing, simply by connecting them to a development machine.

Smaller or common COTS components, like a simple USB cable or piece of hardware, are visually inspected and their proper operation is covered by the quality assurance done on each individual unit.

### Assembly (Protocol & Detailed Instructions)

Our complete assembly work plans are available [in the document repository](https://github.com/votingworks/docs-vxsuite-v4/tree/main/hardware-assets/workplans).

## Quality Assurance Protocols – Integration Testing

### Full System Integration Testing

Many issues only emerge when software is installed on production hardware or when the various components of the system are used together. In order to catch these higher-level system issues, VotingWorks performs full system integration testing before every release.&#x20;

At VotingWorks locations, VotingWorks testing staff set up the full suite of hardware with the latest software release. The testing procedures are designed to imitate an election flow and test any common corner cases or past issues. Most testing procedures are repeated with multiple election packages and system settings to confirm that there are not issues specific to certain configurations.&#x20;

When an issues is found, the issue is immediately escalated to the engineering team for a fix. A new release is created and testing procedures are restarted in full to ensure fixes do not introduce regressions.

We have comprehensive test reports:

* [external testing reports](https://github.com/votingworks/docs-vxsuite-v4/tree/main/quality-assurance/testing/external-testing)
* [internal testing reports](https://github.com/votingworks/docs-vxsuite-v4/tree/main/quality-assurance/testing/internal-testing)

### Production Unit Quality Assurance

Every unit assembled in production is manually tested against a comprehensive checklist to ensure the unit is fully operational. The quality assurance procedures are designed to imitate an election flow and check for any issues found on past units. Checklists for VxAdmin, VxMark, VxScan, and VxCentralScan are public [here in the documentation repository](https://github.com/votingworks/docs-vxsuite-v4/tree/main/quality-assurance/production).
