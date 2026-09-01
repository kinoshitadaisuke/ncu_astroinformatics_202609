#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:01:33 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    #
    # some constants
    #

    # pi
    pi = math.pi
    print (f'pi   = {pi}')

    # tau
    tau = math.tau
    print (f'tau  = 2.0 * pi\n     = {tau}')

    # e
    e = math.e
    print (f'e    = {e}')

    # positive infinity
    pinf = math.inf
    print (f'+inf = {pinf}')

    # negative infinity
    ninf = -math.inf
    print (f'-inf = {ninf}')

    # NaN (not a number)
    nan = math.nan
    print (f'NaN  = {nan}')

# execution of main function
if (__name__ == '__main__'):
    main ()
