#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:48:18 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.table

# main function
def main ():
    # VOTable file
    file_vot = 'exoplanet.vot'

    # reading VOTable file and making an Astropy table
    table_exoplanet = astropy.table.Table.read (file_vot)

    # printing information of planet discovered by direct imaging in 2025
    mask = (table_exoplanet["detection_type"] == "Imaging") \
        & (table_exoplanet["discovered"] == 2025)
    print (table_exoplanet[mask]["name", "mass", "semi_major_axis", \
                                 "orbital_period", "detection_type", \
                                 "discovered"])

# execution of main function
if (__name__ == '__main__'):
    main ()
