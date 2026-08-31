#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:26:29 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # initialisation of a variable "a"
    a_deg = 0.0

    # calculating sin (0 deg), sin (15 deg), sin (30 deg), ..., sin (180 deg)
    while (a_deg <= 180.0):
        # converting from degree into radian
        a_rad = math.radians (a_deg)
        # calculation of sine
        sin_a = math.sin (a_rad)
        # printing result of calculation
        print (f'sin ({a_deg:5.1f} deg) = {sin_a:8.6f}')
        # incrementing variable "a"
        a_deg += 15.0

# execution of main function
if (__name__ == '__main__'):
    main ()
