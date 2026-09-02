#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:21:37 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy arrays using numpy.logspace ()
    a = numpy.logspace (-5.0, 5.0, 11)

    # printing a
    print (f'a = {a}')

    # calculation
    # no need of using "for"
    b = numpy.log10 (a)

    # printing b
    print (f'b = log10 (a) = {b}')

# execution of main function
if (__name__ == '__main__'):
    main ()
