# Disk Space Monitor

Disk Space Monitor is a lightweight utility that checks available storage space on local disks.

The demo version uses sample disk information but can easily be connected to the operating system.

---

## Features

- Scan available drives
- Calculate used percentage
- Detect low free space
- Generate console report
- Warning system

---

## Example

```
Disk Scan

Drive C:
Used: 91%
Status: Warning

Drive D:
Used: 58%
Status: Healthy

Summary

Total drives: 2
Warnings: 1
```

Run

```bash
python app.py
```

No third-party libraries are required.
