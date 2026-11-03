import subprocess
import sys


def ps(command: str) -> list[str]:
    """Run a PowerShell command and return non-empty output lines."""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,
            timeout=20,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        lines = [l.strip() for l in result.stdout.splitlines() if l.strip()]
        return lines or ["N/A"]
    except Exception as e:
        return [f"Error: {e}"]


CHECKS = {
    "Machine GUID (registry)": "(Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\Cryptography').MachineGuid",
    "System UUID": "(Get-CimInstance Win32_ComputerSystemProduct).UUID",
    "Motherboard Serial": "(Get-CimInstance Win32_BaseBoard).SerialNumber",
    "Motherboard Model": "(Get-CimInstance Win32_BaseBoard).Product",
    "BIOS Serial": "(Get-CimInstance Win32_BIOS).SerialNumber",
    "CPU ID": "(Get-CimInstance Win32_Processor).ProcessorId",
    "Disk Serial(s)": "(Get-CimInstance Win32_DiskDrive).SerialNumber",
    "Disk Model(s)": "(Get-CimInstance Win32_DiskDrive).Model",
    "GPU Name(s)": "(Get-CimInstance Win32_VideoController).Name",
    "MAC Address(es)": "(Get-CimInstance Win32_NetworkAdapter | Where-Object {$_.PhysicalAdapter -and $_.MACAddress}).MACAddress",
    "RAM Serial(s)": "(Get-CimInstance Win32_PhysicalMemory).SerialNumber",
}


def main():
    if sys.platform != "win32":
        print("This tool only works on Windows.")
        return

    print("=" * 50)
    print("  HWID Checker")
    print("  Made by @coveredinarchives")
    print("=" * 50)
    for label, cmd in CHECKS.items():
        print(f"\n{label}:")
        for line in ps(cmd):
            print(f"  {line}")
    print("\n" + "=" * 50)
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
