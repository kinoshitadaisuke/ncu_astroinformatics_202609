#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:58:00 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# main function
def main ():
    # tar file
    file_tar = 'files.tar'

    # opening file for reading
    with tarfile.open (file_tar, 'r:*') as fh:
        # extracting files
        fh.extractall ()

# execution of main function
if (__name__ == '__main__'):
    main ()
