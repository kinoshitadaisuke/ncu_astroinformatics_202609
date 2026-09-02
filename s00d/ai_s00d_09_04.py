#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:30:02 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # SFC64 random number generator
    rng = numpy.random.Generator (numpy.random.SFC64 ())

    # generating 10 random numbers of uniform distribution between 100 and 200
    array_x = rng.uniform (1000.0, 2000.0, 30)

    # printing generated random numbers
    print (f'{array_x}')

# execution of main function
if (__name__ == '__main__'):
    main ()
