#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:07:22 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # two integers "c" and "d"
    c = 30
    d = 45

    # lcm
    lcm_c_d = math.lcm (c, d)

    # printing results
    print (f'Use of lcm () function:')
    print (f'  c                                = {c}')
    print (f'  d                                = {d}')
    print (f'  least common multiple of c and d = {lcm_c_d}')
    print (f'')

# execution of main function
if (__name__ == '__main__'):
    main ()
