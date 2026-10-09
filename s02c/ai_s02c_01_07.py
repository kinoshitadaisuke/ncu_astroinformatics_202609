#!/usr/bin/env python3

#
# Time-stamp: <2026/10/05 10:07:42 (UT+08:00) daisuke>
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
    list_interval = [
        'minmax',
        'percentile99.9',
        'percentile99.7',
        'percentile99.5',
        'percentile99.0',
        'percentile95.0',
        'percentile90.0',
        'percentile80.0',
        'percentile70.0',
        'percentile60.0',
        'percentile50.0',
        'zscale',
    ]
    list_stretch = [
        'asinh',
        'histeq',
        'linear',
        'log',
        'sinh',
        'sqrt',
        'squared',
    ]

    # adding arguments
    parser.add_argument ('-i', '--input', default='', \
                         help='input FITS file')
    parser.add_argument ('-o', '--output', default='', \
                         help='output PNG file name')
    parser.add_argument ('-d', '--resolution', type=float, default=225.0, \
                         help='resolution in DPI (default: 225.0)')
    parser.add_argument ('-c', '--cmap', choices=list_cmap, default='gray', \
                         help='colour map (default: gray)')
    parser.add_argument ('-n', '--name', default='', \
                         help='object name')
    parser.add_argument ('-r', '--interval', default=None, \
                         choices=list_interval, \
                         help='choice of interval (default: None)')
    parser.add_argument ('-s', '--stretch', default='linear', \
                         choices=list_stretch, \
                         help='choice of image stretch (default: None)')
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
    image_stretch  = args.stretch
    interval       = args.interval
    verbose        = args.verbose

    # printing input parameters
    if (verbose):
        print (f'#')
        print (f'# Input parameters:')
        print (f'#   object name   : {object_name}')
        print (f'#   input file    : {file_input}')
        print (f'#   output file   : {file_output}')
        print (f'#   resolution    : {resolution_dpi} [DPI]')
        print (f'#   cmap name     : {cmap_name}')
        print (f'#   interval      : {interval}')
        print (f'#   image stretch : {image_stretch}')
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

    # normalisation (interval and stretch)
    if (interval == 'minmax'):
        interval = astropy.visualization.MinMaxInterval ()
    elif (interval == 'percentile99.9'):
        interval = astropy.visualization.PercentileInterval (99.9)
    elif (interval == 'percentile99.7'):
        interval = astropy.visualization.PercentileInterval (99.7)
    elif (interval == 'percentile99.5'):
        interval = astropy.visualization.PercentileInterval (99.5)
    elif (interval == 'percentile99.0'):
        interval = astropy.visualization.PercentileInterval (99.0)
    elif (interval == 'percentile95.0'):
        interval = astropy.visualization.PercentileInterval (95.0)
    elif (interval == 'percentile90.0'):
        interval = astropy.visualization.PercentileInterval (90.0)
    elif (interval == 'percentile80.0'):
        interval = astropy.visualization.PercentileInterval (80.0)
    elif (interval == 'percentile70.0'):
        interval = astropy.visualization.PercentileInterval (70.0)
    elif (interval == 'percentile60.0'):
        interval = astropy.visualization.PercentileInterval (60.0)
    elif (interval == 'percentile50.0'):
        interval = astropy.visualization.PercentileInterval (50.0)
    elif (interval == 'zscale'):
        interval = astropy.visualization.ZScaleInterval ()

    if (image_stretch == 'asinh'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.AsinhStretch () )
    elif (image_stretch == 'histeq'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.HistEqStretch (image) )
    elif (image_stretch == 'linear'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.LinearStretch () )
    elif (image_stretch == 'log'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.LogStretch () )
    elif (image_stretch == 'sinh'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.SinhStretch () )
    elif (image_stretch == 'sqrt'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.SqrtStretch () )
    elif (image_stretch == 'squared'):
        norm \
            = astropy.visualization.mpl_normalize.ImageNormalize \
            ( image, interval=interval, \
              stretch=astropy.visualization.SquaredStretch () )
    
    # plotting image
    if (image_stretch == None):
        im = ax.imshow (image, origin='lower', cmap=cmap_name)
    else:
        im = ax.imshow (image, origin='lower', cmap=cmap_name, norm=norm)
    fig.colorbar (im)
    
    # saving file
    fig.savefig (file_output, dpi=resolution_dpi)

# executing main function
if (__name__ == '__main__'):
    main ()
