#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:09:35 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # conversion from radian into degree
    f_rad = math.pi / 2.0
    f_deg = math.degrees (f_rad)

    # printing result
    print (f'{f_rad} rad = {f_deg} deg')

# execution of main function
if (__name__ == '__main__'):
    main ()
