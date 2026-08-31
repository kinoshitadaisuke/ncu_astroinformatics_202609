#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:15:47 (UT+08:00) daisuke>
#

# main function
def main ():
    # assignment of a value to a variable
    a = 3 + 4j

    # printing the value of a variable using built-in function "print ()"
    print ('a = %f + %fi' % (a.real, a.imag))

# execution of main function
if (__name__ == '__main__'):
    main ()
