#!/usr/bin/env python3

#
# Time-stamp: <2026/10/07 12:17:59 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy
import astropy.io.fits

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# function to read a FITS file
def read_fits (file_fits):
    # reading FITS file
    with astropy.io.fits.open (file_fits) as hdu:
        # reading header and image
        header = hdu[0].header
        wcs    = astropy.wcs.WCS (header)
        image  = hdu[0].data
        # if no image in PrimaryHDU, then read next HDU
        if (header['NAXIS'] == 0):
            header = hdu[1].header
            image  = hdu[1].data
    # returning header and image
    return (image, header, wcs)

# main function
def main ():
    # initialising a parser
    parser = argparse.ArgumentParser (description='Making a colour image')

    # adding arguments
    parser.add_argument ('-b', '--blue', default='b.fits', \
                         help='input file name for blue image')
    parser.add_argument ('-g', '--green', default='g.fits', \
                         help='output file name for green image')
    parser.add_argument ('-r', '--red', default='r.fits', \
                         help='output file name for red image')
    parser.add_argument ('-o', '--output', default='out.fits', \
                         help='output file name')
    parser.add_argument ('-q', '--softening', type=float, default=8.0, \
                         help='asinh softening parameter Q (default: 8)')
    parser.add_argument ('-s', '--stretch', type=float, default=5.0, \
                         help='asinh stretch parameter (default: 5)')
    parser.add_argument ('-n', '--name', default='', \
                         help='name of object')
    parser.add_argument ('-v', '--verbose', action='store_true', \
                         help='verbose mode')

    # parsing arguments
    args = parser.parse_args ()
    
    # input parameters
    file_blue   = args.blue
    file_green  = args.green
    file_red    = args.red
    file_output = args.output
    Q           = args.softening
    stretch     = args.stretch
    object_name = args.name
    verbose     = args.verbose

    # printing input parameters
    if (verbose):
        print (f'#')
        print (f'# Input parameters:')
        print (f'#   file_blue   = {file_blue}')
        print (f'#   file_green  = {file_green}')
        print (f'#   file_red    = {file_red}')
        print (f'#   file_output = {file_output}')
        print (f'#   Q           = {Q}')
        print (f'#   stretch     = {stretch}')
        print (f'#   object name = {object_name}')
        print (f'#   verbose     = {verbose}')
        print (f'#')

    # opening FITS files and reading image data
    (image_blue,  header_blue,  wcs_blue)  = read_fits (file_blue)
    (image_green, header_green, wcs_green) = read_fits (file_green)
    (image_red,   header_red,   wcs_red)   = read_fits (file_red)

    # making a colour image
    image_rgb = astropy.visualization.make_lupton_rgb (image_red, \
                                                       image_green, \
                                                       image_blue, \
                                                       stretch=stretch, \
                                                       Q=Q)
    
    # making a fig object
    fig = matplotlib.figure.Figure ()

    # making a canvas object
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

    # making an axes object
    ax = fig.add_subplot (111, projection=wcs_blue)

    # plotting image
    ax.set_xlabel (f'Right Ascension')
    ax.set_ylabel (f'Declination')
    ax.set_title (f'{object_name}')
    im = ax.imshow (image_rgb)

    # saving the figure to a file
    fig.savefig (file_output, dpi=225.0)
    
# execution of the main function
if (__name__ == '__main__'):
    main ()
    
