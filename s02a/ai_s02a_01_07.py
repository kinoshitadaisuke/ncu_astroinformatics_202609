#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:42:00 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# main function
def main ():
    # units
    u_micron   = astropy.units.micron
    u_Hz       = astropy.units.Hz
    u_GHz      = astropy.units.GHz
    u_spectral = astropy.units.spectral ()

    # wavelength
    wl = 850 * u_micron

    # frequency corresponding to EM wave of wavelength 850 micron
    freq     = wl.to (u_Hz, equivalencies=u_spectral)
    freq_GHz = wl.to (u_GHz, equivalencies=u_spectral)

    # printing result
    print (f'wavelength = {wl:g}  ==>  frequency = {freq:g} = {freq_GHz:g}')

# execution of main function
if (__name__ == '__main__'):
    main ()
