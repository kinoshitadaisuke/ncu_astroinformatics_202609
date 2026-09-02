#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:51:36 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray) using numpy.linspace ()
    array_r = numpy.linspace (1000, 2000, 21)

    # printing Numpy array
    print (f'array_r:\n{array_r}')

    # printing information
    print (f'information:')
    print (f'  ndim     = {array_r.ndim}')
    print (f'  size     = {array_r.size}')
    print (f'  shape    = {array_r.shape}')
    print (f'  dtype    = {array_r.dtype}')
    print (f'  itemsize = {array_r.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
