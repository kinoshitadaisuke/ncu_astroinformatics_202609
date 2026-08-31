#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:17:15 (UT+08:00) daisuke>
#

# main function
def main ():
    # assignment of values to variables
    c  = 299792458
    au = 149597870700
    pc = 3.08567758 * 10**16

    # fancy formatting using formatted string literals
    print (f'c    = {c:g} [m/s]')
    print (f'1 au = {au:g} [m]')
    print (f'1 pc = {pc:g} [m]')

# execution of main function
if (__name__ == '__main__'):
    main ()
