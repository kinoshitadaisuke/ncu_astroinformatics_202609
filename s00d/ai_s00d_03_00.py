#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:49:38 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray) with 10 elements all equal to zeros
    array_k = numpy.zeros ( (10,) )

    # printing Numpy array
    print (f'array_k:\n{array_k}')

    # printing information
    print (f'information:')
    print (f'  ndim     = {array_k.ndim}')
    print (f'  size     = {array_k.size}')
    print (f'  shape    = {array_k.shape}')
    print (f'  dtype    = {array_k.dtype}')
    print (f'  itemsize = {array_k.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
