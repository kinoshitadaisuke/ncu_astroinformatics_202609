#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:24:41 (UT+08:00) daisuke>
#

# main function
def main ():
    # initialisation of a variable "total"
    total = 0

    # calculating 1 + 2 + 3 + ... + 10 using "for" statement
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        # adding "i" to "total"
        total = total + i

    # printing result of calculation
    print (f'1 + 2 + 3 + ... + 8 + 9 + 10 = {total}')

# execution of main function
if (__name__ == '__main__'):
    main ()
