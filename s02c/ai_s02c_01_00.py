#!/usr/bin/env python3

#
# Time-stamp: <2026/10/02 13:07:11 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# importing astroquery module
import astroquery.hips2fits
import astroquery.mast

# main function
def main ():
    # choice of name resolver
    name_resolver = 'SIMBAD'

    # object name
    object_name = 'Omega Centauri'

    # output file name
    file_output = 'omega_centauri_dss2_blue.fits'
    
    # units
    u_deg = astropy.units.deg
    
    # making mast object
    mast = astroquery.mast.Mast ()
    
    # data source
    data_source = 'CDS/P/DSS2/blue'

    # number of pixels
    npix_width  = 2048
    npix_height = 2048

    # RA and Dec
    coords  = mast.resolve_object (object_name, resolver=name_resolver)
    ra_deg  = coords.ra.deg * u_deg
    dec_deg = coords.dec.deg * u_deg

    # field-of-view in deg
    fov_deg = 0.5 * u_deg

    # projection type
    projection_type = 'TAN'

    # file format
    file_format = 'fits'

    # retrieving data
    astroquery.hips2fits.conf.timeout = 300
    fits_hdu = astroquery.hips2fits.hips2fits.query (
        hips=data_source,
        width=npix_width,
        height=npix_height,
        ra=ra_deg,
        dec=dec_deg,
        fov=fov_deg,
        projection=projection_type,
        get_query_payload=False,
        format=file_format,
    )

    # writing data into a FITS file
    fits_hdu.writeto (file_output, overwrite=True)

# execution of main function
if (__name__ == '__main__'):
    main ()
