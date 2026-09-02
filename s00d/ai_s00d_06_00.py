#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:24:39 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # making Numpy array
    a = numpy.linspace (0.0, 10.0, 11)

    # printing A
    print (f'a:\n{a}')

    # accessing to an element by indexing
    print (f'a[0]  = {a[0]}')
    print (f'a[1]  = {a[1]}')
    print (f'a[5]  = {a[5]}')
    print (f'a[-1] = {a[-1]}')
    print (f'a[-3] = {a[-3]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
