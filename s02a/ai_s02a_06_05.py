#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:58:07 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# main function
def main ():
    # input file name
    file_input = 'm3.fits'

    # opening FITS file
    with astropy.io.fits.open (file_input) as hdu_list:
        # printing HDU information
        print (hdu_list.info ())

        # reading FITS header, WCS information, and image data
        header = hdu_list[0].header
        wcs    = astropy.wcs.WCS (header)
        image  = hdu_list[0].data

    # printing data types of the header, wcs, and image
    print (f'type of "header" : {type (header)}')
    print (f'type of "wcs"    : {type (wcs)}')
    print (f'type of "image"  : {type (image)}')

# execution of main function
if (__name__ == '__main__'):
    main ()
