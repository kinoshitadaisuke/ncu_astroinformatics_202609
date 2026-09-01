#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:18:56 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable
    x = sympy.symbols ('x')

    # function y(x)
    y = sympy.Function ('y')

    # Lane-Emden equation of n=0
    lane_emden_n0 = sympy.Eq (x**-2 * (x**2 * y(x).diff (x)).diff (x), -1)

    # printing equation
    print (f'equation: {lane_emden_n0}')

    # solving Lane-Emden equation of n=0
    sol = sympy.dsolve (lane_emden_n0, y(x))

    # printing result
    print (f'solution: {sol}')

# execution of main function
if (__name__ == '__main__'):
    main ()
