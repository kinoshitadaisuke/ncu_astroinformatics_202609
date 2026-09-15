#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 12:02:04 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    #
    # constants
    #

    # speed of light in vacuum
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # printing values and units of constants
    print (f'Constants:')
    print (f'  c = {c[0]:g} [{c[1]}]')
    print (f'  h = {h[0]:g} [{h[1]}]')
    print (f'  k = {k[0]:g} [{k[1]}]')

# execution of main function
if (__name__ == '__main__'):
    main ()
