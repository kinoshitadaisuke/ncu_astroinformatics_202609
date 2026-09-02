#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:29:42 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # random number generator
    rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

    # generating 10 random numbers of uniform distribution between 0 and 1
    array_x = rng.random (10)

    # printing generated random numbers
    print (f'{array_x}')

# execution of main function
if (__name__ == '__main__'):
    main ()
