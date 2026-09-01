#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:29:08 (UT+08:00) daisuke>
#

# importing os module
import os

# main function
def main ():
    # obtaining the value of environmental variable "LANG"
    env_lang = os.environ['LANG']

    # printing the value of environmental variable "LANG"
    print (f'LANG = {env_lang}')

# execution of main function
if (__name__ == '__main__'):
    main ()
