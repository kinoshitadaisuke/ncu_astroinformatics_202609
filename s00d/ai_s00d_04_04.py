#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:53:18 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making a Numpy array
    a = numpy.array ([ [1.0, 2.0, 3.0], [100.0, 200.0, 300.0] ])

    # printing Numpy array "a"
    print (f'a:')
    print (f'{a}')

    # making a transposed array
    b = numpy.transpose (a)

    # printing Numpy array "b"
    print (f'b:')
    print (f'{b}')

# execution of main function
if (__name__ == '__main__'):
    main ()
