#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:46:54 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# main function
def main ():
    # file name
    file_hosts = '/etc/hosts'

    # making a pathlib object
    path_hosts = pathlib.Path (file_hosts)

    # existence check
    if (path_hosts.exists ()):
        print (f'The file "{path_hosts}" exists!')
    else:
        print (f'The file "{path_hosts}" DOES NOT exist!')

# execution of main function
if (__name__ == '__main__'):
    main ()
