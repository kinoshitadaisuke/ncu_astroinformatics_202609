#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:20:25 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy arrays using numpy.linspace ()
    a = numpy.linspace (0.0, 9.0, 10)
    b = numpy.linspace (1.0, 10.0, 10)

    # printing a and b
    print (f'a = {a}')
    print (f'b = {b}')

    # calculation
    # no need of using "for"
    c = a * b

    # printing c
    print (f'c = a * b = {c}')

# execution of main function
if (__name__ == '__main__'):
    main ()
