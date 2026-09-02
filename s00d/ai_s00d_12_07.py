#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:40:41 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# main function
def main ():
    # making a Numpy array
    data = numpy.array ([
        [9.8, 7.6],
        [5.4, 3.2],
        [1.0, -1.2],
        [-3.4, -5.6],
        [-7.8, -9.0],
    ])

    # printing Numpy array
    print (f'{data}')

    # output data file
    file_output = 'numpy_02.data'

    # saving Numpy array into file
    numpy.savetxt (file_output, data, fmt='%8.3f',
                   header='test data created by numpy.savetxt ()')

# execution of main function
if (__name__ == '__main__'):
    main ()
