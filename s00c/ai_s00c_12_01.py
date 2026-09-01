#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:57:43 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# main function
def main ():
    # tar file
    file_tar = 'files.tar'

    # opening file for reading
    with tarfile.open (file_tar, 'r:*') as fh:
        # getting file names in tar file
        list_files = fh.getnames ()

    # for each file name in list
    for filename in list_files:
        # printing file name
        print (filename)

# execution of main function
if (__name__ == '__main__'):
    main ()
