#!/usr/bin/env python3

#
# Time-stamp: <2026/10/01 13:37:27 (UT+08:00) daisuke>
#

# import argparse module
import argparse

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# main function
def main ():
    # initialising a parser
    descr = 'converting a FITS file into a PNG file'
    parser = argparse.ArgumentParser (description=descr)

    # choices
    list_cmap = [
        'gray',
        'bone',
        'cool',
        'hot',
        'copper',
        'viridis',
        'plasma',
        'inferno',
        'magma',
        'cividis',
        'ocean',
        'cubehelix',
        'rainbow',
        'jet',
        'turbo',
    ]

    # adding arguments
    parser.add_argument ('-i', '--input', default='', \
                         help='input FITS file')
    parser.add_argument ('-o', '--output', default='', \
                         help='output PNG file name')
    parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                         help='resolution in DPI (default: 225.0)')
    parser.add_argument ('-c', '--cmap', choices=list_cmap, default='gray', \
                         help='colour map (default: gray)')
    parser.add_argument ('-n', '--name', default='', \
                         help='object name')
    parser.add_argument ('-v', '--verbose', action='count', default=0, \
                         help='verbosity (default: 0)')

    # parsing arguments
    args = parser.parse_args ()

    # input parameters
    file_input     = args.input
    file_output    = args.output
    resolution_dpi = args.resolution
    cmap_name      = args.cmap
    object_name    = args.name
    verbose        = args.verbose

    # printing input parameters
    if (verbose):
        print (f'#')
        print (f'# Input parameters:')
        print (f'#   object name : {object_name}')
        print (f'#   input file  : {file_input}')
        print (f'#   output file : {file_output}')
        print (f'#   resolution  : {resolution_dpi} [DPI]')
        print (f'#   cmap name   : {cmap_name}')
        print (f'#')

    # opening FITS file
    with astropy.io.fits.open (file_input) as list_hdu:
        # reading header, WCS, and image data
        header = list_hdu[0].header
        wcs    = astropy.wcs.WCS (header)
        image  = list_hdu[0].data

    # making fig, canvas, and ax objects
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111, projection=wcs)

    # axes
    ax.set_title (object_name)
    ax.set_xlabel ('Right Ascension')
    ax.set_ylabel ('Declination')

    # normalisation
    norm \
        = astropy.visualization.mpl_normalize.ImageNormalize \
        ( stretch=astropy.visualization.AsinhStretch () )
    
    # plotting image
    im = ax.imshow (image, origin='lower', cmap=cmap_name, norm=norm)
    fig.colorbar (im)
    
    # saving file
    fig.savefig (file_output, dpi=resolution_dpi)

# executing main function
if (__name__ == '__main__'):
    main ()
