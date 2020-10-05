#!/usr/bin/env python

import os
import sys
import shutil
import socket

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
    if gigabytes_free < min_gb or percent_free < min_percent:
       return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_usage(disk="/", min_gb=2, min_percent=10)

def check_no_newtwork():
    """Will return True if it fails to resolve the url False if it succeeds."""
    try:
        socket.gethostbyname("www.google.com") # Raises an exception upon failure
        return False # Success
    except:
        return True # Failure

def main():
    checks=[
    (check_reboot, "Pending Reboot"),
    (check_root_full, "Root partition full"),
    (check_no_newtwork, "No working Network"),
    ]
    everything_ok = True # We want to show more than one message if more than
                         # on check is failing
    for check, mesg in checks:
        if check():
            print(mesg)
            everything_ok = False # Change the variable to false if one of the
                                  # checks finds a problem


    if not everything_ok:
        sys.exit(1) # Exit with an error code Only AFTER having done all the checks


    print("Everything OK.")
    sys.exit(0)

main()
