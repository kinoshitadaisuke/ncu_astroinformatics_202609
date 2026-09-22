#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:38:58 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # Solar mass
    M_S = astropy.constants.M_sun

    # Jupiter mass
    M_J = astropy.constants.M_jup

    # Earth mass
    M_E = astropy.constants.M_earth

    # printing Solar mass, Jupiter mass, and Earth mass
    print (M_S, "\n")
    print (M_J, "\n")
    print (M_E, "\n")

    # value of Jupiter mass in the unit of Solar mass and Earth mass
    print (f'1 M_J = {M_J}')
    print (f'      = {M_J / M_S:g} M_S')
    print (f'      = {M_J / M_E:g} M_E')

# execution of main function
if (__name__ == '__main__'):
    main ()
