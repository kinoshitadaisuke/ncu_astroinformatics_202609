#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:42:52 (UT+08:00) daisuke>
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

# execution of main function
if (__name__ == '__main__'):
    main ()
