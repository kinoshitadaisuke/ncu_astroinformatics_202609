#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:06:29 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two floats "a" and "b"
    a = 12.34
    b = -56.78

    # modf
    (a_fractional, a_integer) = math.modf (a)
    (b_fractional, b_integer) = math.modf (b)

    # printing results
    print (f'Use of modf () function:')
    print (f'  a                    = {a}')
    print (f'  integer part of a    = {a_integer}')
    print (f'  fractional part of a = {a_fractional}')
    print (f'  b                    = {b}')
    print (f'  integer part of b    = {b_integer}')
    print (f'  fractional part of b = {b_fractional}')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
