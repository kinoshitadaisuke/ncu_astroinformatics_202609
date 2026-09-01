#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:47:28 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# main function
def main ():
    # directory name
    dir_zone = '/usr/share/zoneinfo'

    # making a pathlib object
    path_zone = pathlib.Path (dir_zone)

    # finding directory contents
    list_files = path_zone.iterdir ()

    # printing directory contents
    print (f'directory contents of "{path_zone}":')
    for filename in list_files:
        # printing file name
        print (f'  {filename}')

# execution of main function
if (__name__ == '__main__'):
    main ()
