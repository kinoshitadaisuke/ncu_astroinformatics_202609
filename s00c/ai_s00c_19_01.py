#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:14:16 (UT+08:00) daisuke>
#

# importing uncertainties module
import uncertainties

# main function
def main ():
    # quantity "a": 8.0 +/- 0.8
    a = uncertainties.ufloat (8.0, 0.8)

    # quantity "b": 4.0 +/- 0.6
    b = uncertainties.ufloat (4.0, 0.6)

    # calculation of a / b
    c = a / b

    # printing value of "c"
    print (f'a = {a}')
    print (f'b = {b}')
    print (f'c = a / b = {a} / {b} = {c}')

# execution of main function
if (__name__ == '__main__'):
    main ()
