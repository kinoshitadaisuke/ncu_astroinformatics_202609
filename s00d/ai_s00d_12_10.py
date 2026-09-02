#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:41:29 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# main function
def main ():
    # input data file
    file_input = 'numpy_03.npy'

    # loading a Numpy array from npy file
    array_b = numpy.load (file_input)

    # printing Numpy array
    print (f'{array_b}')

    # object type of the object "array_b"
    type_array_b = type (array_b)

    # printing object type
    print (f'object type = {type_array_b}')

    # printing information of Numpy array
    print (f'information:')
    print (f'  ndim     = {array_b.ndim}')
    print (f'  size     = {array_b.size}')
    print (f'  shape    = {array_b.shape}')
    print (f'  dtype    = {array_b.dtype}')
    print (f'  itemsize = {array_b.itemsize} byte')

# execution of main function
if (__name__ == '__main__'):
    main ()
