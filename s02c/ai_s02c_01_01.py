#!/usr/bin/env python3

#
# Time-stamp: <2026/09/30 12:40:06 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# main function
def main ():
    # input FITS file name
    file_fits = 'omega_centauri_dss2_blue.fits'

    # output PNG file name
    file_png = 'omega_centauri_dss2_blue.png'

    # resolution in DPI
    resolution_dpi = 225.0

    # colour map name
    cmap_name = 'viridis'

    # object name
    object_name = 'Omega Centauri'

    # opening FITS file
    with astropy.io.fits.open (file_fits) as list_hdu:
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
    
    # printing status
    print (f'{file_fits} ==> {file_png}')

    # saving file
    fig.savefig (file_png, dpi=resolution_dpi)

# executing main function
if (__name__ == '__main__'):
    main ()
