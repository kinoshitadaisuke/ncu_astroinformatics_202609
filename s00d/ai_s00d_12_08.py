#!/usr/bin/env python3

#
# Time-stamp: <2026/09/02 09:40:58 (UT+08:00) daisuke>
#

# main function
def main ():
    # input data file
    file_input = 'numpy_02.data'

    # opening file for reading
    with open (file_input, 'r') as fh_in:
        # reading data in the file line-by-line
        for line in fh_in:
            # removing line feed at the end of the line
            line = line.rstrip ()
            # printing data
            print (f'{line}')

# execution of main function
if (__name__ == '__main__'):
    main ()
