#!/usr/bin/env python3

#
# Time-stamp: <2026/10/28 10:22:11 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# main function
def main ():
    # allow insecure downloading
    ssl._create_default_https_context = ssl._create_unverified_context

    # URL of data file
    url_data = 'https://faculty.washington.edu/ivezic/linear/allDataFinal/allLINEARfinal_dat.tar.gz'

    # output file name
    file_output = 'linear.tar.gz'

    # printing status
    print (f'Now, fetching {url_data}...')

    # opening URL
    with urllib.request.urlopen (url_data) as fh_read:
        # reading data
        data_byte = fh_read.read ()

    # printing status
    print (f'Finished fetching {url_data}!')

    # printing status
    print (f'Now, writing data into file "{file_output}"...')

    # opening file for writing
    with open (file_output, 'wb') as fh_write:
        # writing data
        fh_write.write (data_byte)

    # printing status
    print (f'Finished writing data into file "{file_output}"!')

# executing main function
if (__name__ == '__main__'):
    main ()
