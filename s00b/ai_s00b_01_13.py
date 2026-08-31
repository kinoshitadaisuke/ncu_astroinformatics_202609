#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:23:16 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # (x, y) coordinate
    x, y = +1.0, -1.0

    # calculation of arctangent
    a_rad = math.atan2 (y, x)

    # conversion from radian into degree
    a_deg = math.degrees (a_rad)

    # printing result of calculation
    print (f'x            = {x}')
    print (f'y            = {y}')
    print (f'atan2 (y, x) = {a_rad} rad = {a_deg} deg')

# execution of main function
if (__name__ == '__main__'):
    main ()
