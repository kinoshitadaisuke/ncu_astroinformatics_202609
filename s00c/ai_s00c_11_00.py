#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 12:01:01 (UT+08:00) daisuke>
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
    url_numbers = 'https://s3b.astro.ncu.edu.tw/ai_202609/data/numbers.data.gz'

    # output data file
    file_numbers = 'numbers.data.gz'

    # opening URL
    with urllib.request.urlopen (url_numbers) as fh_in:
        # reading data
        data_numbers = fh_in.read ()

    # opening file for writing
    with open (file_numbers, 'wb') as fh_out:
        # writing data into file
        fh_out.write (data_numbers)

# execution of main function
if (__name__ == '__main__'):
    main ()
