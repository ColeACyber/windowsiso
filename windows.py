import subprocess

def flash_windows_iso(iso_path, flash_drive):
    try:
        # Use dd to write the Windows ISO to the flash drive
        subprocess.run(['sudo', 'dd', 'if=' + iso_path, 'of=' + flash_drive, 'bs=4M', 'status=progress'])
        print("Windows ISO successfully flashed to the flash drive.")
    except Exception as e:
        print(f"Error flashing Windows ISO: {e}")

if __name__ == "__main__":
    # Replace 'path/to/windows.iso' with the actual path to your Windows 11 ISO
    windows_iso_path = 'path/to/windows.iso'
    
    # Replace '/dev/sdX' with the actual device path of your flash drive
    flash_drive_path = '/dev/sdX'

    flash_windows_iso(windows_iso_path, flash_drive_path)
