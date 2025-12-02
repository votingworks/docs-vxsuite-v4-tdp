# Guidance for Test Labs

This page covers guidance for test labs that isn't relevant for election workers.

## Power Cycling

While test labs are free to run machines for long periods of time and naturally need to for tests like the 104-hour continuous operations test, we generally recommend powering down machines every couple of days. Rebooting a machine triggers necessary log file compression and rotation to save disk space. While some log files are compressed and rotated automatically on a daily basis, others are not in order to maintain the highest possible fidelity and are only compressed and rotated on reboot.
