#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:17:00 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# main function
def main ():
    # nano
    nano = scipy.constants.nano

    # wavelength of electromagnetic radiation
    wavelength = 500.0 * nano

    # frequency of electromagnetic radiation
    frequency = scipy.constants.lambda2nu (wavelength)

    # printing the result of conversion
    print (f'{wavelength:g} [m] ==> {frequency:g} [Hz]')

# execution of main function
if (__name__ == '__main__'):
    main ()
