#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:23:52 (UT+08:00) daisuke>
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

    # eigenvalues and eigenvectors of matrix A
    eigenvalvec = scipy.linalg.eig (A)

    # printing eigenvalues and eigenvectors of matrix A
    print (f'eigenvalues of matrix A:\n{eigenvalvec[0]}')
    print (f'eigenvectors of matrix A:\n{eigenvalvec[1]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
