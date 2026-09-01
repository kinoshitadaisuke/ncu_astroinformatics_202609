#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:12:21 (UT+08:00) daisuke>
#

# main function
def main ():
    # two floating point numbers "a" and "b"
    a = 1.2
    b = 2.4

    # calculation of c = a + b
    c = a + b

    # printing result of calculation
    print (f'{a} + {b}             = {c}')

    # the other calculations
    d = 1.1
    e = 1.1
    f = 1.1
    g = d + e
    h = d + e + f
    i = d + e + f - 3.3
    print (f'{d} + {e}             = {g}')
    print (f'{d} + {e} + {f}       = {h}')
    print (f'{d} + {e} + {f} - 3.3 = {i}')

# execution of main function
if (__name__ == '__main__'):
    main ()
