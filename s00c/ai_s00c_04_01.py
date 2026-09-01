#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:47:11 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# main function
def main ():
    # file name
    file_resolv = '/etc/resolv.conf'

    # making a pathlib object
    path_resolv = pathlib.Path (file_resolv)

    # printing parent, name, suffix, stem
    print (f'parent, name, suffix, and stem of "{path_resolv}":')
    print (f'  parent of "{path_resolv}" = "{path_resolv.parent}"')
    print (f'  name of "{path_resolv}"   = "{path_resolv.name}"')
    print (f'  suffix of "{path_resolv}" = "{path_resolv.suffix}"')
    print (f'  stem of "{path_resolv}"   = "{path_resolv.stem}"')

# execution of main function
if (__name__ == '__main__'):
    main ()
