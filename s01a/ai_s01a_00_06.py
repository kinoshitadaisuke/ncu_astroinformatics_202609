#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:16:11 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    # some units for length
    angstrom = scipy.constants.angstrom
    au       = scipy.constants.au
    ly       = scipy.constants.light_year
    parsec   = scipy.constants.parsec

    # printing units for length
    print (f'1 angstrom = {angstrom:g} [m]')
    print (f'1 au       = {au:g} [m]')
    print (f'1 ly       = {ly:g} [m]')
    print (f'1 parsec   = {parsec:g} [m]')

# execution of main function
if (__name__ == '__main__'):
    main ()
