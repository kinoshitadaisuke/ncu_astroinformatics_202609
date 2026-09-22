#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:39:17 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # Solar radius
    R_S = astropy.constants.R_sun

    # Jupiter radius
    R_J = astropy.constants.R_jup

    # Earth radius
    R_E = astropy.constants.R_earth

    # printing Solar radius, Jupiter radius, and Earth radius
    print (R_S, "\n")
    print (R_J, "\n")
    print (R_E, "\n")

    # value of 1 Earth radius in the unit of Solar radius
    print (f'1 R_E = {R_E:g}')
    print (f'      = {R_E / R_S:g} R_S')

# execution of main function
if (__name__ == '__main__'):
    main ()
