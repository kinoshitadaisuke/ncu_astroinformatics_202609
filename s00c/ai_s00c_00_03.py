#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:26:11 (UT+08:00) daisuke>
#

# importing os module
import os

# main function
def main ():
    # target directory
    dir_target = '/bin'

    # obtaining a list of files and directories at the directory "dir_target"
    list_files = os.listdir (path=dir_target)

    # printing files and directories
    print (f'list of files and directories at "{dir_target}":')
    # for each file (or directory) in the list
    for filename in list_files:
        # printing name of file (or directory)
        print (f'  {filename}')

# execution of main function
if (__name__ == '__main__'):
    main ()
