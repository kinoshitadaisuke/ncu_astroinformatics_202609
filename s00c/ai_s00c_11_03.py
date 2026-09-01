#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:57:05 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# main function
def main ():
    # data file
    file_data = 'numbers.data'

    # output file
    file_output = 'numbers_2.data.gz'

    # opening file for reading
    with open (file_data, 'r') as fh_in:
        # reading file
        data_str = fh_in.read ()

    # converting string into raw byte
    data_byte = data_str.encode ('utf-8')

    # opening file for writing
    with gzip.open (file_output, 'wb') as fh_out:
        # writing compressed data into file
        fh_out.write (data_byte)

# execution of main function
if (__name__ == '__main__'):
    main ()
