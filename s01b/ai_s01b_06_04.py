#!/usr/bin/env python3

#
# Time-stamp: <2026/09/10 16:18:37 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# main function
def main ():
    # database file
    file_db = 'landolt_2009.db'

    # connecting to a new database
    with duckdb.connect (file_db) as connection:
        # getting a list of tables
        tables = connection.sql ('SHOW TABLES').df ()
        # printing a list of tables
        print (tables)

# execution of main function
if (__name__ == '__main__'):
    main ()
