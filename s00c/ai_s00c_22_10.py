#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:18:40 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # function y
    y = sympy.Function ('y')

    # variable x
    x, k = sympy.symbols ('x k')

    # dy/dx
    dy_dx = sympy.diff (y(x), x)

    # differential equation
    eq = sympy.Eq (dy_dx, -k*y(x))

    # solving dy/dx = -ky
    sol = sympy.dsolve (eq, y(x))

    # printing result
    print (f'equation: {eq}')
    print (f'solution: {sol}')

# execution of main function
if (__name__ == '__main__'):
    main ()
