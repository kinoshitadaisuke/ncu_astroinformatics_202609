#!/usr/bin/env python3

#
# Time-stamp: <2026/09/10 16:21:51 (UT+08:00) daisuke>
#

# importing duckdb module
import duckdb

# main function
def main ():
    # database file
    file_db = 'landolt_2009.db'

    # SQL comand to create a table
    sql_maketable = "CREATE TABLE landolt" \
        + " (name TEXT PRIMARY KEY, ra TEXT, dec TEXT," \
        + " ra_deg DOUBLE, dec_deg DOUBLE, mag_v DOUBLE," \
        + " colour_bv DOUBLE, colour_ub DOUBLE, colour_vr DOUBLE," \
        + " colour_ri DOUBLE, colour_vi DOUBLE, nobs INTEGER, nnight INTEGER);"

    # connecting to a new database
    with duckdb.connect (file_db) as connection:
        # executing a SQL command
        connection.sql (sql_maketable)

# execution of main function
if (__name__ == '__main__'):
    main ()
