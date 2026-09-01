#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:09:18 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # conversion from degree into radian
    e_deg = 180.0
    e_rad = math.radians (e_deg)

    # printing result
    print (f'{e_deg} deg = {e_rad} rad')

# execution of main function
if (__name__ == '__main__'):
    main ()
