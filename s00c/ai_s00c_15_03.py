#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:06:10 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two floats "a" and "b"
    a = 12.34
    b = -56.78

    # trunc
    a_trunc = math.trunc (a)
    b_trunc = math.trunc (b)

    # printing results
    print (f'Use of trunc () function:')
    print (f'  a         = {a}')
    print (f'  trunc (a) = {a_trunc}')
    print (f'  {a_trunc} is the integer part of {a}.')
    print (f'  b         = {b}')
    print (f'  trunc (b) = {b_trunc}')
    print (f'  {b_trunc} is the integer part of {b}.')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
