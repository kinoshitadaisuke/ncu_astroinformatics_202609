#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:43:09 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# main function
def main ():
    # input data file
    file_input = 'numpy_05.npz'

    # loading Numpy arrays from npy file
    arrays = numpy.load (file_input)

    # printing "arrays"
    print (f'{arrays}')

    # printing object type of "arrays"
    print (f'{type (arrays)}')

    # first Numpy array in "arrays"
    array_e = arrays['array_e']

    # second Numpy array in "arrays"
    array_f = arrays['array_f']

    # third Numpy array in "arrays"
    array_g = arrays['array_g']

    # printing array_c and array_d
    print (f'array_e:')
    print (array_e)
    print (f'array_f:')
    print (array_f)
    print (f'array_g:')
    print (array_g)

# execution of main function
if (__name__ == '__main__'):
    main ()
