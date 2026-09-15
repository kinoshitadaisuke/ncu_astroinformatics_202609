#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:35:29 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# main function
def main ():
    # CSV file name
    file_csv = 'hyg/hyg/v3/hyg_v38.csv.gz'

    # reading a CSV file and storing data in an astropy table
    table = astropy.io.ascii.read (file_csv, format='csv')

    # printing astropy table
    print (table)

# execution of main function
if (__name__ == '__main__'):
    main ()
