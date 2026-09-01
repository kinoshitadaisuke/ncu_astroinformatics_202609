#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:59:32 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# main function
def main ():
    # file of Yale Bright Star Catalogue
    file_bsc = 'catalog.gz'

    # making pathlib object
    path_bsc = pathlib.Path (file_bsc)

    # existence check of file
    if (path_bsc.exists ()):
        print (f'File "{file_bsc}" exists.')
        print (f'Downloading of Yale Bright Star Catalogue was successfully done!')
    else:
        print (f'File "{file_bsc}" DOES NOT exist.')
        print (f'Download Yale Bright Star Catalogue!')

# execution of main function
if (__name__ == '__main__'):
    main ()
