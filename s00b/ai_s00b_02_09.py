#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:27:14 (UT+08:00) daisuke>
#

# main function
def main ():
    # printing odd number between 0 and 30
    for i in range (30):
        # if number is divisible by 2, then skipping to next number
        if (i % 2 == 0):
            continue
        # if not, then it is an odd number
        print (f'{i} is an odd number.')

# execution of main function
if (__name__ == '__main__'):
    main ()
