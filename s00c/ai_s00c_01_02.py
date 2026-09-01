#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:44:09 (UT+08:00) daisuke>
#

# importing sys module
import sys

# main function
def main ():
    # receiving command-line arguments
    args = sys.argv

    # number of command-line arguments
    n_args = len (args)

    # printing number of command-line arguments
    print (f'number of command-line arguments = {n_args}')

    # printing command-line arguments
    print (f'arguments = {args}')

# execution of main function
if (__name__ == '__main__'):
    main ()
