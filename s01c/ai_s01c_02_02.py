#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:36:41 (UT+08:00) daisuke>
#

# importing json module
import json

# main function
def main ():
    # JSON file name
    file_json = 'exoplanets/data/exoplanet.json'

    # opening file
    with open (file_json, 'r') as fh:
        # reading JSON file
        data = json.load (fh)

    # printing keys of the data
    for key in data[0].keys ():
        print (f"{key}")

# execution of main function
if (__name__ == '__main__'):
    main ()
