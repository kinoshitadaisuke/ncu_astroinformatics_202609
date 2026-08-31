#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:16:33 (UT+08:00) daisuke>
#

# main function
def main ():
    # assignment of values to variables by multiple assignment
    a, b = 1.2, 3.4

    # calculation
    c = a * b

    # printing values of variables using built-in function "print ()"
    # and printf-style string formatting
    print ('%f * %f = %f' % (a, b, c) )

# execution of main function
if (__name__ == '__main__'):
    main ()
