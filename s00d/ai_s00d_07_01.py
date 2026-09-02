#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:26:02 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array
    a = numpy.linspace (0.0, 10.0, 11)

    # printing "a"
    print (f'a:\n{a}')

    # trying a.copy ()
    b = a.copy ()

    # printing "b"
    print (f'b:\n{b}')

    # IDs of "a" and "b"
    print (f'id (a) = {id (a)}')
    print (f'id (b) = {id (b)}')

    # changing "a[5]"
    a[5] += 10

    # printing "a"
    print (f'a:\n{a}')

    # printing "b"
    print (f'b:\n{b}')

    # IDs of "a" and "b"
    print (f'id (a) = {id (a)}')
    print (f'id (b) = {id (b)}')

# execution of main function
if (__name__ == '__main__'):
    main ()
