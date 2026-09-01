#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:12:53 (UT+08:00) daisuke>
#

# importing decimal module
import decimal

# main function
def main ():
    # calculation of sqrt (2.0)
    a = decimal.Decimal ('2.0')
    b = a.sqrt ()

    # result of calculation
    print (f'a = {a}')
    print (f'b = sqrt (a) = sqrt ({a}) = {b}')

    # calculation of log10 (12.3)
    c = decimal.Decimal ('12.3')
    d = c.log10 ()

    # result of calculation
    print (f'c = {c}')
    print (f'd = log10 (c) = log10 ({c}) = {d}')

# execution of main function
if (__name__ == '__main__'):
    main ()
