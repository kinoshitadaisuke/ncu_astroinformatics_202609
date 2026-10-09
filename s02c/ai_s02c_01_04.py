#!/usr/bin/env python3

#
# Time-stamp: <2026/10/02 13:06:49 (UT+08:00) daisuke>
#

# import argparse module
import argparse

# importing astropy module
import astropy.units

# importing astroquery module
import astroquery.hips2fits
import astroquery.mast

# main function
def main ():
    # initialising a parser
    descr = 'downloading astronomical image of a given target object names'
    parser = argparse.ArgumentParser (description=descr)

    # choices
    list_resolver = [
        'SIMBAD',
        'NED',
    ]
    list_survey = [
        'CDS/P/DSS2/blue',
        'CDS/P/DSS2/red',
        'CDS/P/DSS2/NIR',
        'CDS/P/SDSS9/u',
        'CDS/P/SDSS9/g',
        'CDS/P/SDSS9/r',
        'CDS/P/SDSS9/i',
        'CDS/P/SDSS9/z',
    ]
    
    # adding arguments
    parser.add_argument ('object', nargs=1, \
                         help='target object name')
    parser.add_argument ('-o', '--output', default='', \
                         help='output file name')
    parser.add_argument ('-r', '--resolver', default='SIMBAD', \
                         choices=list_resolver, \
                         help='name resolver (default: SIMBAD)')
    parser.add_argument ('-x', '--width', type=int, default=2048, \
                         help='width of image in pixel (default: 2048)')
    parser.add_argument ('-y', '--height', type=int, default=2048, \
                         help='height of image in pixel (default: 2048)')
    parser.add_argument ('-f', '--fov', type=float, default=30.0, \
                         help='field-of-view in arcmin (default: 30)')
    parser.add_argument ('-p', '--projection', default='TAN', \
                         help='projectino type (default: TAN)')
    parser.add_argument ('-s', '--survey', default='CDS/P/DSS2/blue', \
                         choices=list_survey, \
                         help='data source (default: CDS/P/DSS2/blue)')
    parser.add_argument ('-v', '--verbose', action='count', default=0, \
                         help='verbosity (default: 0)')

    # parsing arguments
    args = parser.parse_args ()

    # input parameters
    object_name     = args.object[0]
    file_output     = args.output
    name_resolver   = args.resolver
    npix_width      = args.width
    npix_height     = args.height
    fov_arcmin      = args.fov
    projection_type = args.projection
    data_source     = args.survey
    verbose         = args.verbose

    # units
    u_deg = astropy.units.deg
    u_arcmin = astropy.units.arcmin

    # field-of-view
    fov = fov_arcmin * u_arcmin
    
    # making mast object
    mast = astroquery.mast.Mast ()
    
    # RA and Dec
    coords  = mast.resolve_object (object_name, resolver=name_resolver)
    ra      = coords.ra
    dec     = coords.dec

    # file format
    file_format = 'fits'

    # printing input parameters
    if (verbose):
        print (f'#')
        print (f'# Input parameters:')
        print (f'#   data source   : {data_source}')
        print (f'#   name resolver : {name_resolver}')
        print (f'#   object name   : {object_name}')
        print (f'#   RA            : {ra}')
        print (f'#   Dec           : {dec}')
        print (f'#   output file   : {file_output}')
        print (f'#   width         : {npix_width} [pix]')
        print (f'#   height        : {npix_height} [pix]')
        print (f'#   field-of-view : {fov_arcmin} [arcmin]')
        print (f'#   projection    : {projection_type}')
        print (f'#')
    
    # retrieving data
    astroquery.hips2fits.conf.timeout = 300
    fits_hdu = astroquery.hips2fits.hips2fits.query (
        hips=data_source,
        width=npix_width,
        height=npix_height,
        ra=ra,
        dec=dec,
        fov=fov,
        projection=projection_type,
        get_query_payload=False,
        format=file_format,
    )

    # writing data into a FITS file
    fits_hdu.writeto (file_output, overwrite=True)

# execution of main function
if (__name__ == '__main__'):
    main ()
