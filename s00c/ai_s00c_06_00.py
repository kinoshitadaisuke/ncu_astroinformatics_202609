#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:49:30 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# main function
def main ():
    # executing a command "date"
    subprocess.run ('date')

# execution of main function
if (__name__ == '__main__'):
    main ()
