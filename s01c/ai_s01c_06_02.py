#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:43:23 (UT+08:00) daisuke>
#

# importing json module
import json

# main function
def main ():
    # file name
    file_json = 'osc_0000_1989/SN1989V.json'

    # opening file
    with open (file_json, 'r') as fh:
        # reading JSON data from file
        data = json.load (fh)

    # printing data
    for obj in data:
        print ("obj =", obj)
        for key in data[obj]:
            print ("  %-16s ==> %s" % (key, data[obj][key]) )

# execution of main function
if (__name__ == '__main__'):
    main ()
