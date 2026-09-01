#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:05:54 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two floats "a" and "b"
    a = 12.34
    b = -56.78

    # ceil
    a_ceil = math.ceil (a)
    b_ceil = math.ceil (b)

    # printing results
    print (f'Use of ceil () function:')
    print (f'  a         = {a}')
    print (f'  ceil (a)  = {a_ceil}')
    print (f'  {a_ceil} is the smallest integer greater than or equal to {a}.')
    print (f'  b         = {b}')
    print (f'  ceil (b)  = {b_ceil}')
    print (f'  {b_ceil} is the smallest integer greater than or equal to {b}.')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
