#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:48:56 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# main function
def main ():
    # date/time in UT as a string
    time_str = '2026-01-01T12:00:00'

    # constructing Astropy's Time object from a string
    time = astropy.time.Time (time_str, format='isot', scale='utc')

    # calculating JD and MJD
    time_jd  = time.jd
    time_mjd = time.mjd

    # printing JD and MJD
    print (f'{time} (UT) = JD {time_jd} = MJD {time_mjd}')

# execution of main function
if (__name__ == '__main__'):
    main ()
