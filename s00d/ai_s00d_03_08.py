#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:51:51 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray) using numpy.logspace ()
    array_s = numpy.logspace (0, 5, 11)

    # printing Numpy array
    print (f'array_s:\n{array_s}')

    # printing information
    print (f'information:')
    print (f'  ndim     = {array_s.ndim}')
    print (f'  size     = {array_s.size}')
    print (f'  shape    = {array_s.shape}')
    print (f'  dtype    = {array_s.dtype}')
    print (f'  itemsize = {array_s.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
