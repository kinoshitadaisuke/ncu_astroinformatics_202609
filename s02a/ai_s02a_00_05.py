#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:38:40 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # astronomical unit
    au = astropy.constants.au

    # printing au
    print (au, "\n")

    # parsec
    pc = astropy.constants.pc

    # km/s
    unit_km = astropy.units.km

    # printing pc
    print (pc, "\n")

    # 1 au
    print (f'1 au = {au:g}')
    print (f'     = {au.to (unit_km):g}')

    # 1 pc
    print (f'1 pc = {pc:g}')
    print (f'     = {pc / au} au')

# execution of main function
if (__name__ == '__main__'):
    main ()
