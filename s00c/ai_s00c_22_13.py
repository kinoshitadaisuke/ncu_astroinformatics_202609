#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:19:27 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f(x)
    f = sympy.sqrt (4 - x**2)

    # integration of f(x) from 0 to 2
    I = sympy.integrate (f, (x, 0, 2))

    # printing result
    print (f'I = {I}')

# execution of main function
if (__name__ == '__main__'):
    main ()
