#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:57:50 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits

# main function
def main ():
    # input file name
    file_input = 'm3.fits'

    # opening FITS file
    with astropy.io.fits.open (file_input) as hdu_list:
        # printing HDU information
        print (hdu_list.info ())

# execution of main function
if (__name__ == '__main__'):
    main ()
