#!/usr/bin/env python3

#
# Time-stamp: <2026/11/09 10:44:39 (UT+08:00) daisuke>
#

# importing rebound module
import rebound

# main function
def main ():
    # name of simulation file
    file_sim = 'star_planet.bin'

    # reading a simulation from a file
    sim = rebound.Simulation (file_sim)

    # printing simulation object
    print (sim)

# executing main function
if (__name__ == '__main__'):
    main ()
