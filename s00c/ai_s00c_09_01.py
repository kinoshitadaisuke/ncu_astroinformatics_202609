#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:52:43 (UT+08:00) daisuke>
#

# importing csv module
import csv

# main function
def main ():
    # CSV file name
    file_csv = 'stars.csv'

    # opening file for reading
    with open (file_csv, 'r') as fh:
        data_elements = csv.reader (fh)
        # printing data
        for line in data_elements:
            # spectral type
            spectype = line[0]
            # effective temperature
            try:
                t_eff = float (line[1])
            except:
                continue
            # absolute magnitude
            try:
                absmag = float (line[2])
            except:
                continue
            # luminosity
            try:
                luminosity = float (line[3])
            except:
                continue
            # printing data
            print (f'{spectype}')
            print (f'  effective temperature [K]     : {t_eff:7.1f}')
            print (f'  absolute magnitude            : {absmag:+5.1f}')
            print (f'  luminosity [solar luminosity] : {luminosity:10.3f}')

# execution of main function
if (__name__ == '__main__'):
    main ()
