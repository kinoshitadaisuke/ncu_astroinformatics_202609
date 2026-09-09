#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:15:49 (UT+08:00) daisuke>
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
        print (f'  value = {scipy.constants.value (constant)}')
        print (f'  error = {scipy.constants.precision (constant)}')
        print (f'  unit  = {scipy.constants.unit (constant)}')

# execution of main function
if (__name__ == '__main__'):
    main ()
