#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:06:46 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two floats "a" and "b"
    a = 12.34
    b = -56.78

    # fabs
    a_abs = math.fabs (a)
    b_abs = math.fabs (b)

    # printing results
    print (f'Use of fabs () function:')
    print (f'  a                   = {a}')
    print (f'  absolute value of a = {a_abs}')
    print (f'  b                   = {b}')
    print (f'  absolute value of b = {b_abs}')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
