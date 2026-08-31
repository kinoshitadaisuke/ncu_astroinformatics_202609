#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:20:32 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # a number
    a = 3.0

    # calculation of square root
    b = math.sqrt (a)
    c = a**0.5

    # printing result of calculation
    print (f'a = {a}')
    print (f'b = math.sqrt ({a}) = {b}')
    print (f'c = a^0.5 = {a}^0.5 = {c}')

# execution of main function
if (__name__ == '__main__'):
    main ()
