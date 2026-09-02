#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:24:04 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array (3x3 matrix)
    C = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

    # printing C
    print (f'C:\n{C}')

    # making Numpy array (3x3 unit matrix)
    E3 = numpy.identity (3)

    # printing E3
    print (f'E3:\n{E3}')

    # calculation
    D = E3 @ C

    # printing D
    print (f'D = E3 @ C:\n{D}')

# execution of main function
if (__name__ == '__main__'):
    main ()
