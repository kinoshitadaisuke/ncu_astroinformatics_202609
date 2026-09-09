#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:24:09 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# main function
def main ():
    # matrix A
    A = numpy.array ( [ [3.0, 1.0], [2.0, 2.0] ] )

    # printing matrix A
    print (f'matrix A:\n{A}')

    # the other way to get eigenvalues of matrix A
    eigenvalues = scipy.linalg.eigvals (A)

    # printing eigenvalues of matrix A
    print (f'eigenvalues of matrix A:\n{eigenvalues}')

# execution of main function
if (__name__ == '__main__'):
    main ()
