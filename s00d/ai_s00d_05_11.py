#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:22:59 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy arrays (2x2 matrix)
    A = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])
    B = numpy.array ([ [4.0, 2.0], [1.0, 3.0] ])

    # printing A and B
    print (f'A:\n{A}')
    print (f'B:\n{B}')

    # matrix product
    C = A @ B

    # printing C
    print (f'C = A @ B:\n{C}')

# execution of main function
if (__name__ == '__main__'):
    main ()
