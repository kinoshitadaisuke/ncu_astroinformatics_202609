#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:17:17 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f
    f = sympy.sin (x)

    # differentiation of f(x)
    df_dx = sympy.diff (f, x)

    # printing result
    print (f'f(x)  = {f}')
    print (f'df/dx = {df_dx}')

# execution of main function
if (__name__ == '__main__'):
    main ()
