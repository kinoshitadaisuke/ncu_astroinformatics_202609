#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:37:30 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # speeed of light in vacuum
    c = astropy.constants.c

    # calculation
    v = 0.01 * c

    # printing c and v
    print (f'c = {c}')
    print (f'v = 0.01 * {c}')
    print (f'  = {v}')

# execution of main function
if (__name__ == '__main__'):
    main ()
