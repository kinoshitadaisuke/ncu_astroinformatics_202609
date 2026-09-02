#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:28:01 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array
    a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

    # printing "a"
    print (f'a:\n{a}')

    # in-place sorting using ".sort ()" method
    a.sort ()

    # printing "a"
    print (f'a:\n{a}')

# execution of main function
if (__name__ == '__main__'):
    main ()
