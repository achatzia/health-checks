#!/usr/bin/env python

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
        """Returns True if there isn't enough disk space, False otherwise."""
	du = shutil.disk_usage(disk)
	# calculate percent of free space
	percent_free = 100 * du.free / du.total
	# calculate free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
	    return True
	return False

def main():
    if check_reboot():
       print("Pending Reboot mate.")
       sys.exit(1)
    if check_disk_usage(disk="/", min_gb=2, min_percent=10):
	print("Disk full!")
	sys.exit(1)
    print("Everything OK.")
    sys.exit(0)

main()
