#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:19:58 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable
    x = sympy.symbols ('x')

    # function f(x)
    f = x**4 * sympy.exp (-x**2)

    # positive infinity
    pinf = sympy.oo

    # integration of f(x) from 0 to infinity
    I = sympy.integrate (f, (x, 0, pinf))

    # printing result
    print (f'I = {I}')

# execution of main function
if (__name__ == '__main__'):
    main ()
