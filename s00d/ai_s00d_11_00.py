#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:34:47 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # sample Numpy array
    a = numpy.array ([10.0, 10.1, 9.9, 10.2, 9.8, 10.3, 9.7, \
                      300.0, 10.0, 10.0, 9.9, 9.9, 10.1, 10.1, 10.0])

    # making a mask
    mask = numpy.array ([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

    # making a masked array
    a_masked = numpy.ma.array (a, mask=mask)

    # printing array "a"
    print (f'a:')
    print (f'{a}')

    # printing mask "mask"
    print (f'mask:')
    print (f'{mask}')

    # printing masked array "a_masked"
    print (f'a_masked:')
    print (f'{a_masked}')

# execution of main function
if (__name__ == '__main__'):
    main ()
