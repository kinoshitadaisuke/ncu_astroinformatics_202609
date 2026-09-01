#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:10:07 (UT+08:00) daisuke>
#

# importing math module
import math

# main function
def main ():
    # distance between two points
    coord_0  = (0.0, 1.0)
    coord_1  = (3.0, 2.0)
    dist_0_1 = math.dist (coord_0, coord_1)
    coord_2  = (0.0, 0.0, 0.0)
    coord_3  = (1.0, 1.0, 1.0)
    dist_2_3 = math.dist (coord_2, coord_3)

    # printing result
    print (f'coord_0 = {coord_0}')
    print (f'coord_1 = {coord_1}')
    print (f'distance between coord_0 and coord_1 = {dist_0_1}')
    print (f'coord_2 = {coord_2}')
    print (f'coord_3 = {coord_3}')
    print (f'distance between coord_2 and coord_3 = {dist_2_3}')

# execution of main function
if (__name__ == '__main__'):
    main ()
