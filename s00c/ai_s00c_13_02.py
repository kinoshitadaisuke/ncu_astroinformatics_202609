#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:58:52 (UT+08:00) daisuke>
#

# importing zipfile module
import zipfile

# main function
def main ():
    # zip file
    file_zip = 'files2.zip'

    # opening file for reading
    with zipfile.ZipFile (file_zip, 'r') as fh:
        # extracting files
        fh.extractall ()

# execution of main function
if (__name__ == '__main__'):
    main ()
