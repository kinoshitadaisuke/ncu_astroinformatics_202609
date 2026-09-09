#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:43:00 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.special

# main function
def main ():
    # calculation of Gamma (6)
    result = scipy.special.gamma (6)

    # printing result of calculation
    print (f'Gamma (6) = 5! = {result}')

# execution of main function
if (__name__ == '__main__'):
    main ()
