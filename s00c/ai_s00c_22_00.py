#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:15:56 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f
    f = (x + 1)**2

    # expansion of (x+1)**2
    f2 = sympy.expand (f)

    # printing result
    print (f'{f} = {f2}')

# execution of main function
if (__name__ == '__main__'):
    main ()
