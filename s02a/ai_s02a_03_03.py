#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:49:30 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# main function
def main ():
    # getting current date/time
    now = astropy.time.Time.now ()

    # printing date/time
    print (f'now  = {now}')
    print (f'     = JD  {now.jd:14.6f}')
    print (f'     = MJD {now.mjd:14.6f}')

# execution of main function
if (__name__ == '__main__'):
    main ()
