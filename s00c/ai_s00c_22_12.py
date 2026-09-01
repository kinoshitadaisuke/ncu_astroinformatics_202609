#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:19:12 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f(x)
    f = -x + 1

    # integration of f(x) from 0 to 1
    I = sympy.integrate (f, (x, 0, 1))

    # printing result
    print (f'I = {I}')

# execution of main function
if (__name__ == '__main__'):
    main ()
