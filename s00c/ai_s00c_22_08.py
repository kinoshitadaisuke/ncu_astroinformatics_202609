#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:18:06 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f
    f = sympy.sin (x)

    # integration of f(x)
    I = sympy.integrate (f, x)

    # printing result
    print (f'f(x)  = {f}')
    print (f'integration of f(x) = {I}')

# execution of main function
if (__name__ == '__main__'):
    main ()
