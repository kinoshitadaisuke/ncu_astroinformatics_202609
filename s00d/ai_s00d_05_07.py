#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:21:53 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy arrays using numpy.linspace ()
    a_deg = numpy.linspace (0.0, 180.0, 7)

    # printing a_deg
    print (f'a_deg = {a_deg}')

    # angle in radian
    a_rad = a_deg / 180.0 * numpy.pi

    # printing a_rad
    print (f'a_rad = {a_rad}')

    # calculation
    # no need of using "for"
    sin_a = numpy.sin (a_rad)
    cos_a = numpy.cos (a_rad)

    # printing b
    print (f'sin (a) = {sin_a}')
    print (f'cos (a) = {cos_a}')

# execution of main function
if (__name__ == '__main__'):
    main ()
