#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:25:26 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array
    a = numpy.array ([ [0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], \
                       [8.0, 9.0, 10.0, 11.0], [12.0, 13.0, 14.0, 15.0] ])

    # printing A
    print (f'a:\n{a}')

    # accessing to an element by indexing
    print (f'a[0:2,1:3]:\n{a[0:2,1:3]}')
    print (f'a[1:3,:]:\n{a[1:3,:]}')
    print (f'a[:,1:3]:\n{a[:,1:3]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
