#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:48:59 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray) with a specified data type
    # numpy.dtype ('U10') : 10-character Unicode string
    array_j = numpy.array (['Ceres', 'Pallas', 'Juno', 'Vesta', 'Astraea', \
                            'Hebe', 'Iris', 'Flora', 'Metis', 'Hygiea'], \
                           dtype=numpy.dtype ('U10') )

    # printing Numpy array
    print (f'array_j:\n{array_j}')

    # printing information
    print (f'information:')
    print (f'  ndim     = {array_j.ndim}')
    print (f'  size     = {array_j.size}')
    print (f'  shape    = {array_j.shape}')
    print (f'  dtype    = {array_j.dtype}')
    print (f'  itemsize = {array_j.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
