#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:17:18 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    # giga
    giga = scipy.constants.giga

    # frequency of electromagnetic radiation
    frequency = 115.0 * giga

    # wavelength of electromagnetic radiation
    wavelength = scipy.constants.nu2lambda (frequency)

    # printing the result of conversion
    print (f'{frequency:g} [Hz] ==> {wavelength:g} [m]')

# execution of main function
if (__name__ == '__main__'):
    main ()
