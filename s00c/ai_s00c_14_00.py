#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:59:12 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# main function
def main ():
    # allow insecure downloading
    ssl._create_default_https_context = ssl._create_unverified_context

    # URL of Yale Bright Star Catalogue
    url_bsc = 'https://cdsarc.cds.unistra.fr/ftp/V/50/catalog.gz'

    # output file name
    file_bsc = 'catalog.gz'

    # printing status
    print (f'Now, opening {url_bsc}...')

    # opening URL
    with urllib.request.urlopen (url_bsc) as fh_read:
        # reading data
        data_byte = fh_read.read ()

    # printing status
    print (f'Retrieved data from {url_bsc}!')

    # printing status
    print (f'Now, writing data to file "{file_bsc}"...')

    # opening file for writing
    with open (file_bsc, 'wb') as fh_write:
        # writing data
        fh_write.write (data_byte)

    # printing status
    print (f'Finished writing data to file "{file_bsc}"!')

# execution of main function
if (__name__ == '__main__'):
    main ()
