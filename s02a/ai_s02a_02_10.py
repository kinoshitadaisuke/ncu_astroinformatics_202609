#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:47:07 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.table

# main function
def main ():
    # VOTable file
    file_vot = 'exoplanet.vot'

    # reading VOTable file and making an Astropy table
    table_exoplanet = astropy.table.Table.read (file_vot)

    # printing name, mass, semimajor axis, orbital period, detection type,
    # and year of discovery of exoplanets
    print (table_exoplanet["name", "mass", "semi_major_axis", \
                           "orbital_period", "detection_type", "discovered"])

# execution of main function
if (__name__ == '__main__'):
    main ()
