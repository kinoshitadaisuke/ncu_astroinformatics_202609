#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:11:01 (UT+08:00) daisuke>
#

# importing random module
import random

# main function
def main ():
    # initialisation of random number generator
    random.seed ()

    #
    # generating 10 random numbers of Gaussian dist. of mean=100 and stddev=10
    #

    # parameters
    mean   = 100.0
    stddev = 10.0

    # generating 10 random numbers
    print (f'10 random numbers of Gaussian distribution', \
           f'of mean={mean} and stddev={stddev}')
    for i in range (10):
        # generation of a random number of Gaussian distribution
        r = random.gauss (mean, stddev)
        # printing generated random number
        print (f'  {r:15.11f}')

# execution of main function
if (__name__ == '__main__'):
    main ()
