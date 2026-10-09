#!/usr/bin/env python3

#
# Time-stamp: <2026/10/09 13:03:44 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing PIL module
import PIL.Image

# main function
def main ():
    # width of image in pixel
    width = 1024
    # height of image in pixel
    height = 1024
    # output file name
    file_output = 'test_01.png'
    
    # blue channel image
    image_b = numpy.ones ( (height, width), dtype=numpy.uint8)
    # green channel image
    image_g = numpy.ones ( (height, width), dtype=numpy.uint8)
    # red channel image
    image_r = numpy.ones ( (height, width), dtype=numpy.uint8)

    # changing pixel values
    for i in range (height):
        for j in range (width):
            image_b[i, j] = int (256.0 * (i + j) / (height + width))
            image_g[j, i] = int (256.0 * (i + j) / (height + width))
            image_r[i, j] = int (256.0 * i / height)
    
    # RGB data of image
    image_rgb = numpy.dstack ( (image_r, image_g, image_b) )
    # making colour image
    image_colour = PIL.Image.fromarray (image_rgb)
    # saving image into a file
    image_colour.save (file_output)

    # printing information of Numpy arrays
    print (f'image_b:')
    print (image_b)
    print (f'image_g:')
    print (image_g)
    print (f'image_r:')
    print (image_r)
    print (f'image_colour:')
    print (image_colour)

# execution of main function
if (__name__ == '__main__'):
    main ()
