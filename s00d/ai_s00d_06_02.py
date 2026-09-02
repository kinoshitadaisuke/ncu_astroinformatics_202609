#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:25:11 (UT+08:00) daisuke>
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
    print (f'a[2:5] = {a[2:5]}')
    print (f'a[6:]  = {a[6:]}')
    print (f'a[:3]  = {a[:3]}')
    print (f'a[:]   = {a[:]}')
    print (f'a[-3:] = {a[-3:]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
