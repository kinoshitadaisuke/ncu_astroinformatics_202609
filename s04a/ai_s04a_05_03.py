#!/usr/bin/env python3

#
# Time-stamp: <2026/11/09 10:47:58 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# main function
def main ():
    # ffmpeg command
    ffmpeg = 'ffmpeg'

    # ffmpeg options
    options_ffmpeg = f'-f image2 -start_number 0 -framerate 30' \
        + f' -i comets/comets_%04d.png' \
        + f' -an -vcodec libx264 -pix_fmt yuv420p -threads 16'

    # output file name
    file_output = 'comets.mp4'

    # command to be executed
    command_ffmpeg = f'{ffmpeg} {options_ffmpeg} {file_output}'

    # execution of command
    subprocess.run (command_ffmpeg, shell=True)

# executing main function
if (__name__ == '__main__'):
    main ()
