#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:19:43 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f(x)
    f = sympy.exp (-x**2)

    # positive infinity
    pinf = sympy.oo

    # negative infinity
    ninf = -sympy.oo

    # integration of f(x)
    I = sympy.integrate (f, (x, ninf, pinf))

    # printing result
    print (f'I = {I}')

# execution of main function
if (__name__ == '__main__'):
    main ()
