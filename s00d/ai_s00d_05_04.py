#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:21:01 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy arrays using numpy.linspace ()
    a = numpy.linspace (0.0, 10.0, 11)

    # printing a
    print (f'a = {a}')

    # calculation
    # no need of using "for"
    b = a**2

    # printing b
    print (f'b = a**2 = {b}')

# execution of main function
if (__name__ == '__main__'):
    main ()
