#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:09:52 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # sin (), cos (), and tan ()
    g_deg = 60.0
    g_rad = math.radians (g_deg)
    sin_g = math.sin (g_rad)
    cos_g = math.cos (g_rad)
    tan_g = math.tan (g_rad)

    # printing result
    print (f'{g_deg} deg       = {g_rad} rad')
    print (f'sin ({g_deg} deg) = {sin_g}')
    print (f'cos ({g_deg} deg) = {cos_g}')
    print (f'tan ({g_deg} deg) = {tan_g}')

# execution of main function
if (__name__ == '__main__'):
    main ()
