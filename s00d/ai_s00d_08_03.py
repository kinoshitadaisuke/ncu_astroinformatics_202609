#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:27:30 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array
    a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

    # printing "a"
    print (f'a:\n{a}')

    # sorting by descending order
    b = numpy.sort (a, kind="heapsort") [::-1]

    # printing "b"
    print (f'b = numpy.sort (a, kind="heapsort") [::-1]:\n{b}')

# execution of main function
if (__name__ == '__main__'):
    main ()
