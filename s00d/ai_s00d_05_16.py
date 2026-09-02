#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:24:20 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array (2x2 matrix)
    A = numpy.array ([ [5.0, 3.0], [6.0, 4.0] ])

    # printing A
    print (f'A:\n{A}')

    # calculating inverse matrix of A
    B = numpy.linalg.inv (A)

    # priting B
    print (f'B = A^-1:\n{B}')

    # calculation of A @ B
    C = A @ B

    # printing C
    print (f'C = A @ B:\n{C}')

# execution of main function
if (__name__ == '__main__'):
    main ()
