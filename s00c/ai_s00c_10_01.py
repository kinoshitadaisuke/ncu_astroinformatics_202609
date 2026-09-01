#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:55:18 (UT+08:00) daisuke>
#

# importing json module
import json

# main function
def main ():
    # json file
    file_json = 'stars.json'

    # opening file for reading
    with open (file_json, 'r') as fh:
        # reading json file
        dic_data = json.load (fh)

    # printing data
    for key1 in sorted (dic_data.keys ()):
        print (f'{key1}')
        for key2 in sorted (dic_data[key1].keys ()):
            print (f'  {key2} : {dic_data[key1][key2]}')

# execution of main function
if (__name__ == '__main__'):
    main ()
