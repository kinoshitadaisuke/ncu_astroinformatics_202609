#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:37:15 (UT+08:00) daisuke>
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

    # host star name
    star = 'Kepler-90'

    # printing header
    print (f'List of known exoplanets around star "{star}":')

    # printing the information of exoplanet hosted by Kepler-90
    for i in range (len (data)):
        if (data[i]['star_name'] == 'Kepler-90'):
            print (f"  Exoplanet name: {data[i]['# name']:32s}")
            print (f"    M      = {data[i]['mass']} [M_jupiter]")
            print (f"    a      = {data[i]['semi_major_axis']} [au]")
            print (f"    P      = {data[i]['orbital_period']:} [day]")
            print (f"    method = {data[i]['detection_type']}")

# execution of main function
if (__name__ == '__main__'):
    main ()
