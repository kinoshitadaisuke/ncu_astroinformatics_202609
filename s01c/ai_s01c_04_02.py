#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:40:07 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# main function
def main ():
    # file
    file_data = 'ned1d_new.csv'

    # reading CSV data
    rawdata = astropy.io.ascii.read (file_data, format='csv')

    # printing astropy table summary information
    print (rawdata.info ())

# execution of main function
if (__name__ == '__main__'):
    main ()
