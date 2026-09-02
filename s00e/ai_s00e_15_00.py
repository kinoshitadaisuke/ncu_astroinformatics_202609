#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 14:58:38 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits

# main function
def main ():
    # input FITS file name
    file_fits = 'hltau_alma.fits'

    # opening FITS file
    with astropy.io.fits.open (file_fits) as hdu_list:
        # printing basic information of FITS file
        print (hdu_list.info ())

# execution of main function
if (__name__ == '__main__'):
    main ()
