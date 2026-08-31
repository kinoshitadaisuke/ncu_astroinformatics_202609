#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:17:38 (UT+08:00) daisuke>
#

# main function
def main ():
    # assignment of variables
    c  = 299792458
    au = 149597870700
    pc = 3.08567758 * 10**16

    # fancy formatting using .format () method
    print ('c    = {:g} [m/s]'.format (c))
    print ('1 au = {:g} [m]'.format (au))
    print ('1 pc = {:g} [m]'.format (pc))

# execution of main function
if (__name__ == '__main__'):
    main ()
