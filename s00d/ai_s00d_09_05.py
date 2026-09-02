#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:30:20 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # random number generator
    rng = numpy.random.Generator (numpy.random.Philox ())

    # generating 100 random numbers of Gaussian distribution
    # of mean of 100.0 and standard deviation of 10.0
    array_x = rng.normal (100.0, 10.0, 100)

    # printing generated random numbers
    print (f'{array_x}')

# execution of main function
if (__name__ == '__main__'):
    main ()
