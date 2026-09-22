#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:38:22 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# main function
def main ():
    # gravitational constant
    G = astropy.constants.G

    # printing G
    print (G, "\n")

    # Boltzmann constant
    k = astropy.constants.k_B

    # printing k
    print (k, "\n")

    # Stafan-Boltzmann constant
    sigma = astropy.constants.sigma_sb

    # printing sigma
    print (sigma, "\n")

# execution of main function
if (__name__ == '__main__'):
    main ()
