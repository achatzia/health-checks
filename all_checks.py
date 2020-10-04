#!/usr/bin/env python

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
       print("Pending Reboot mate.")
       sys.exit(1)
    print("Everything OK.")
    sys.exit(0)

main()
