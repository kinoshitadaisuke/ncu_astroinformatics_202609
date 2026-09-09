#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:15:09 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    # searching constants
    search_result = scipy.constants.find ('light')

    # printing search result
    for constant in search_result:
        print (f'{constant}')

# execution of main function
if (__name__ == '__main__'):
    main ()
