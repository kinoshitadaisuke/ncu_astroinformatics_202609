#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:24:18 (UT+08:00) daisuke>
#

# importing sys module
import sys

# main function
def main ():
    # reading an integer number from keyboard typing
    a_str = input ('Type one integer number: ')

    # converting a string into integer
    try:
        a = int (a_str)
    except:
        print (f'ERROR: failed to convert string "{a_str}" into integer!')
        sys.exit (1)

    # if and else statements
    if (a > 0):
        print ("The number you type is a positive number.")
    elif (a < 0):
        print ("The number you type is a negative number.")
    else:
        print ("The number you type is zero.")

# execution of main function
if (__name__ == '__main__'):
    main ()
