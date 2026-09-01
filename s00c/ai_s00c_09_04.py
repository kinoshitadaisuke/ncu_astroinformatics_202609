#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:53:43 (UT+08:00) daisuke>
#

# main function
def main ():
    # data file
    file_data = 'planets_solsys.data'

    # opening file for reading
    with open (file_data, 'r') as fh:
        # reading file line-by-line
        for line in fh:
            # if the line starts with '#'
            if (line[0] == '#'):
                # then, skip
                continue
            # splitting the line into three fields
            (name, mass_str, diameter_str) = line.split ()
            # converting string into float
            try:
                mass = float (mass_str)
            except:
                continue
            try:
                diameter = float (diameter_str)
            except:
                continue
            # printing data
            print (f'{name}')
            print (f'  mass [kg]    : {mass:g}')
            print (f'  diameter [m] : {diameter:g}')

# execution of main function
if (__name__ == '__main__'):
    main ()
