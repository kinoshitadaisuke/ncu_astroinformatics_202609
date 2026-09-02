#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 14:41:47 (UT+08:00) daisuke>
#

# importing numpy
import numpy

# main function
def main ():
    # making a list
    list_a = [0.1, 2.3, 4.5, 6.7, 8.9]

    # making a Numpy array (ndarray)
    array_a = numpy.array (list_a)

    # type of "list_a"
    type_list_a = type (list_a)

    # type of "array_a"
    type_array_a = type (array_a)

    # printing list
    print (f'list_a:')
    print (f'  list_a  = {list_a}')
    print (f'  type    = {type_list_a}')

    # printing Numpy array
    print (f'array_a:')
    print (f'  array_a = {array_a}')
    print (f'  type    = {type_array_a}')

# execution of main function
if (__name__ == '__main__'):
    main ()
