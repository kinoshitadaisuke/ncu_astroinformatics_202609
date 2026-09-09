#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:15:28 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    # searching constants
    search_result = scipy.constants.find ('light')

    # printing search result
    for constant in search_result:
        print (f'{constant}:')
        print (f'  value = {scipy.constants.physical_constants[constant][0]}')
        print (f'  error = {scipy.constants.physical_constants[constant][2]}')
        print (f'  unit  = {scipy.constants.physical_constants[constant][1]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
