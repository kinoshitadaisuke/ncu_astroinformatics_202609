#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:37:47 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # speeed of light in vacuum
    c = astropy.constants.c

    # calculation
    v = 0.01 * c

    # object type of "c"
    type_c = type (c)

    # object type of "v"
    type_v = type (v)

    # printing object type of "c"
    print (f'type of "c" = {type_c}')

    # printing object type of "v"
    print (f'type of "v" = {type_v}')

# execution of main function
if (__name__ == '__main__'):
    main ()
