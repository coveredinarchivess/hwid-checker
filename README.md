# HWID Checker

A small Windows console utility that displays hardware identifiers reported by the system. Made by **@coveredinarchives**.

## Download and run

Download the uploaded `hwid_checker.exe` from this repository and run it on a Windows PC. The console lists the identifiers and waits for Enter before closing.

## Build from source

Requires Windows and Python 3.10 or later. To run the Python script directly:

```powershell
python hwid_checker.py
```

To create a single-file executable with [PyInstaller](https://pyinstaller.org/):

```powershell
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --onefile --console --name hwid_checker hwid_checker.py
```

The output will be `dist/hwid_checker.exe`.

## Identifiers displayed

The checker queries the Windows Machine GUID, system UUID, motherboard model and serial, BIOS serial, CPU ID, disk models and serials, GPU names, physical network adapter MAC addresses, and RAM serials.

## Notes

This tool uses PowerShell and Windows CIM queries, so it is intended for Windows only. Some systems may return blank, generic, or unavailable values. Hardware identifiers can be sensitive; share the output carefully.
