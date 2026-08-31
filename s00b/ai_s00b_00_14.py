#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:17:57 (UT+08:00) daisuke>
#

# main function
def main ():
    # assignment of variables
    c  = 299792458
    au = 149597870700
    pc = 3.08567758 * 10**16

    # fancy formatting using .format () method
    print ('c    = {:g} [m/s]\n1 au = {:g} [m]\n1 pc = {:g} [m]'.format (c, au, pc))

# execution of main function
if (__name__ == '__main__'):
    main ()
