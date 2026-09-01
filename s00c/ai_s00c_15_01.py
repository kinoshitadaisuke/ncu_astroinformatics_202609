#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:05:35 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two floats "a" and "b"
    a = 12.34
    b = -56.78

    # floor
    a_floor = math.floor (a)
    b_floor = math.floor (b)

    # printing results
    print (f'Use of floor () function:')
    print (f'  a         = {a}')
    print (f'  floor (a) = {a_floor}')
    print (f'  {a_floor} is the largest integer less than or equal to {a}.')
    print (f'  b         = {b}')
    print (f'  floor (b) = {b_floor}')
    print (f'  {b_floor} is the largest integer less than or equal to {b}.')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
