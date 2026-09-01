#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:53:01 (UT+08:00) daisuke>
#

# importing csv module
import csv

# main function
def main ():
    # CSV file name
    file_csv = 'stars.csv'

    # opening file for reading
    with open (file_csv, 'r') as fh:
        data_elements = csv.DictReader (fh)
        # printing data
        for line in data_elements:
            print (f'{line["spectral type"]}')
            print (f'  temperature [K]               : {line["temperature [K]"]}')
            print (f'  absolute magnitude            : {line["absolute magnitude"]}')
            print (f'  luminosity [solar luminosity] : {line["luminosity [solar luminosity]"]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
