#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:41:29 (UT+08:00) daisuke>
#

# importing Numpy module
import numpy

# main function
def main ():
    # making a Numpy array (ndarray)
    array_a = numpy.array ([0.1, 2.3, 4.5, 6.7, 8.9])

    # type of "array_a"
    type_array_a = type (array_a)

    # printing type of "array_a"
    print (f'type of "array_a" = {type_array_a}')

# execution of main function
if (__name__ == '__main__'):
    main ()
