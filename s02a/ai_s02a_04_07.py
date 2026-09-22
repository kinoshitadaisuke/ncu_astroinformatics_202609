#!/usr/bin/env python3

#
# Time-stamp: <2026/09/22 13:53:47 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.coordinates

# main function
def main ():
    # RA and Dec of Betelgeuse
    ra_str  = '05h55m10.3s'
    dec_str = '+07d24m25s'

    # making a SkyCoord object
    betelgeuse = astropy.coordinates.SkyCoord (ra=ra_str, dec=dec_str, \
                                               frame='icrs', equinox='J2000')
    (betelgeuse_ra, betelgeuse_dec) = betelgeuse.to_string ('hmsdms').split ()

    # conversion between equatorial system and galactic system
    betelgeuse_gal = betelgeuse.galactic
    betelgeuse_l   = betelgeuse_gal.l
    betelgeuse_b   = betelgeuse_gal.b

    # printing coordinate of Betelgeuse
    print (f'Coordinate of Betelgeuse:')
    print (f'  (RA, Dec) = ({betelgeuse_ra}, {betelgeuse_dec})')
    print (f'  (l, b)    = ({betelgeuse_l}, {betelgeuse_b})')

# execution of main function
if (__name__ == '__main__'):
    main ()
