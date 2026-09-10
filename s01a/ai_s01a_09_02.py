#!/usr/bin/env python3

#
# Time-stamp: <2026/09/10 14:11:29 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.special

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# main function
def main ():
    # output file name
    file_output = 'ai_s01a_09_02.png'

    # values of x
    array_x = numpy.linspace (-6.0, +6.0, 20001)

    # calculation of gamma function
    array_y = scipy.special.gamma (array_x)

    # printing (x, y)
    print (f'array_x:')
    print (f'{array_x}')
    print (f'array_y:')
    print (f'{array_y}')

    # making objects "fig" and "ax"
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # axes
    ax.set_xlabel ('X')
    ax.set_ylabel ('Y')
    ax.grid ()
    ax.set_ylim (-50.0, +50.0)

    # plotting data
    ax.plot (array_x, array_y, \
             linestyle='-', linewidth=3, color='red', \
             label='gamma function')

    # legend
    ax.legend ()

    # saving file
    fig.savefig (file_output, dpi=100)

# execution of main function
if (__name__ == '__main__'):
    main ()
