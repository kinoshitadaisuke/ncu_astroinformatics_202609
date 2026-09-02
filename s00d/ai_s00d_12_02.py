#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:39:17 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# main function
def main ():
    # input data file
    file_input = 'numpy_00.data'

    # opening and reading file and storing data in a Numpy array
    data = numpy.loadtxt (file_input)

    # printing data
    print (f'{data}')

# execution of main function
if (__name__ == '__main__'):
    main ()
