#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:15:11 (UT+08:00) daisuke>
#

# importing pint module
import pint

# main function
def main ():
    # units
    ur           = pint.UnitRegistry ()
    u_km         = ur.km
    u_sec        = ur.sec
    u_km_per_sec = u_km / u_sec

    # velocity
    v = 300.0 * u_km_per_sec

    # time
    t = 10.0 * u_sec

    # calculation of distance travelled
    d = v * t

    # printing result
    print (f'velocity           = {v}')
    print (f'time               = {t}')
    print (f'distance travelled = {d}')

# execution of main function
if (__name__ == '__main__'):
    main ()
