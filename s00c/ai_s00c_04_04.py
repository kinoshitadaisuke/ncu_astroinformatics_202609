#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:48:06 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# main function
def main ():
    # file
    file_pi1000 = 'pi_1000.txt'

    # making a pathlib object
    path_pi1000 = pathlib.Path (file_pi1000)

    # opening file
    with path_pi1000.open () as fh:
        # reading file
        data_pi = fh.read ()

    # printing file content
    print (f'---------- {file_pi1000} ----------')
    print (f'{data_pi}')
    print (f'---------- {file_pi1000} ----------')

# execution of main function
if (__name__ == '__main__'):
    main ()
