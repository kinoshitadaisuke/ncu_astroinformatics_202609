#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 11:59:00 (UT+08:00) daisuke>
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
    url_planets = 'https://s3b.astro.ncu.edu.tw/ai_202609/data/planets_solsys.data'

    # output data file
    file_planets = 'planets_solsys.data'

    # opening URL
    with urllib.request.urlopen (url_planets) as fh_in:
        # reading data
        data_planets = fh_in.read ()

    # opening file for writing
    with open (file_planets, 'w') as fh_out:
        # writing data into file
        fh_out.write (data_planets.decode ('utf-8'))

# execution of main function
if (__name__ == '__main__'):
    main ()
