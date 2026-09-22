#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:55:04 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.stats

# main function
def main ():
    # parameters for random number generation
    mean   = 1000.0
    stddev = 30.0
    n      = 10**4

    # generation of a set of random number of Gaussian distribution
    rng  = numpy.random.default_rng ()
    data = rng.normal (loc=mean, scale=stddev, size=n)

    # printing generated data
    print (f'Genearated random numbers:')
    print (f'{data}')
    print (f'Number of random numbers generated: {len (data)}')

# execution of main function
if (__name__ == '__main__'):
    main ()
