#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:21:21 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # a number
    a = 2.7183

    # calculation of natural logarithm
    b = math.log (a)

    # printing result of calculation
    print (f'a = {a}')
    print (f'b = log (a) = log ({a}) = {b}')

# execution of main function
if (__name__ == '__main__'):
    main ()
