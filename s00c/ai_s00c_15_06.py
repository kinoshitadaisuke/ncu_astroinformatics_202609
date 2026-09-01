#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:07:04 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two integers "c" and "d"
    c = 30
    d = 45

    # gcd
    gcd_c_d = math.gcd (c, d)

    # printing results
    print (f'Use of gcd () function:')
    print (f'  c                                  = {c}')
    print (f'  d                                  = {d}')
    print (f'  greatest common divisor of c and d = {gcd_c_d}')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
