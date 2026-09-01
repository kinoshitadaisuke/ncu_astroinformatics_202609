#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:16:12 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f
    f = x**2 + x - 2

    # factorisation of f
    f2 = sympy.factor (f)

    # printing result
    print (f'{f} = {f2}')

# execution of main function
if (__name__ == '__main__'):
    main ()
