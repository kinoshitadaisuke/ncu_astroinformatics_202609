#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:25:05 (UT+08:00) daisuke>
#

# importing os module
import os

# main function
def main ():
    # knowing where I am now
    cwd = os.getcwd ()

    # printing where you are now
    print (f'currently working directory = "{cwd}"')

# execution of main function
if (__name__ == '__main__'):
    main ()
