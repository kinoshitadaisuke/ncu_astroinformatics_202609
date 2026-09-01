#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:16:28 (UT+08:00) daisuke>
#

# importing sympy module
import sympy

# main function
def main ():
    # variable x
    x = sympy.symbols ('x')

    # function f
    f = (1 + 1/x)**x

    # limit x --> infinity
    lim_f = sympy.limit (f, x, sympy.oo)

    # printing result
    print (f'lim x->infty [{f}] = {lim_f}')

# execution of main function
if (__name__ == '__main__'):
    main ()
