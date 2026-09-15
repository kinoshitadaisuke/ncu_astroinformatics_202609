#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:34:56 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# main function
def main ():
    # CSV file name
    file_csv = 'honey-badger/examples/planets/planets.csv'

    # reading a CSV file and storing data in an astropy table
    table = astropy.io.ascii.read (file_csv, format='csv')

    # printing the information about Jupiter
    mask = (table['Planet'] == 'JUPITER')
    print (f'{table[mask]["Planet", "Number of Moons"]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
