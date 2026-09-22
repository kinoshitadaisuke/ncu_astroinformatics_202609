#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:43:12 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# main function
def main ():
    # units
    u_K        = astropy.units.K
    u_keV      = astropy.units.keV
    u_T_energy = astropy.units.temperature_energy ()

    # energy
    energy = 1.0 * u_keV

    # calculation of equivalent temperature for energy of 1 keV
    T = energy.to (u_K, equivalencies=u_T_energy)

    # printing result
    print (f'energy = {energy:g}  ==>  temperature = {T:g}')

# execution of main function
if (__name__ == '__main__'):
    main ()
