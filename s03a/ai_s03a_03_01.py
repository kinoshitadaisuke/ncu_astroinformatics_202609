#!/usr/bin/env python3

#
# Time-stamp: <2026/10/20 12:19:17 (UT+08:00) daisuke>
#

# importing tarfile module
import tarfile

# main function
def main ():
    # gzipped tar file
    file_targz = 'linear.tar.gz'

    # target directory for extraction of files
    dir_target = 'linear'

    # opening tar file
    with tarfile.open (file_targz, 'r:gz') as fh_targz:
        # extracting files
        fh_targz.extractall (path=dir_target)

# executing main function
if (__name__ == '__main__'):
    main ()
