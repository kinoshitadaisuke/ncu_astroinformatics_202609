#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:51:20 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray) using numpy.arange ()
    array_q = numpy.arange (0, 30, 2)

    # printing Numpy array
    print (f'array_q:\n{array_q}')

    # printing information
    print (f'information:')
    print (f'  ndim     = {array_q.ndim}')
    print (f'  size     = {array_q.size}')
    print (f'  shape    = {array_q.shape}')
    print (f'  dtype    = {array_q.dtype}')
    print (f'  itemsize = {array_q.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
