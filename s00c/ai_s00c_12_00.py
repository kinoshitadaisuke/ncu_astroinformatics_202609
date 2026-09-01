#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 12:01:24 (UT+08:00) daisuke>
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
    url_tarfile = 'https://s3b.astro.ncu.edu.tw/ai_202609/data/files.tar'

    # output data file
    file_tarfile = 'files.tar'

    # opening URL
    with urllib.request.urlopen (url_tarfile) as fh_in:
        # reading data
        data_tarfile = fh_in.read ()

    # opening file for writing
    with open (file_tarfile, 'wb') as fh_out:
        # writing data into file
        fh_out.write (data_tarfile)

# execution of main function
if (__name__ == '__main__'):
    main ()
