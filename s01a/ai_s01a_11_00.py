#!/usr/bin/env python3

#
# Time-stamp: <2026/09/09 13:46:41 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# main function
def main ():
    # output data file
    file_output = 'ai_s01a_11_00.data'

    # pi
    pi = numpy.pi

    # amplitude
    A = 2.0

    # frequency in Hz
    f = 11.0

    # initial phase
    delta = 0.5 * pi

    # baseline
    b = 3.0

    # number of data points
    n = 8192

    # data acquisition interval in sec
    dt = 0.005

    # time
    t = numpy.linspace (0.0, n * dt, n, endpoint=False)

    # synthetic data for FFT
    y = A * numpy.sin (2.0 * pi * f * t - delta) + b

    # opening file for writing
    with open (file_output, 'w') as fh:
        # for all the data
        for i in range (n):
            # writing data into file
            fh.write (f'{t[i]:12.6f}  {y[i]:12.9f}\n')

# execution of main function
if (__name__ == '__main__'):
    main ()
