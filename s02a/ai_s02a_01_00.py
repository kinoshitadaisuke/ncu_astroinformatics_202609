#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:39:57 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# main function
def main ():
    # units
    u_sec = astropy.units.s

    # a quantity object of 900.0 sec
    t = 900.0 * u_sec

    # printing t
    print (f't = {t}')

# execution of main function
if (__name__ == '__main__'):
    main ()
