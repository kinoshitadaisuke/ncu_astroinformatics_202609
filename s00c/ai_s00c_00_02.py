#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:25:50 (UT+08:00) daisuke>
#

# importing os module
import os

# main function
def main ():
    # target directory
    dir_target = '/bin'

    # printing status
    print (f'now, changing directory to "{dir_target}"...')

    # changing directory
    os.chdir (dir_target)

    # printing status
    print (f'finished changing directory to "{dir_target}"!')

    # knowing where I am now
    cwd = os.getcwd ()

    # printing where I am now
    print (f'currently working directory = "{cwd}"')

    # obtaining a list of files and directories in currently working directory
    list_files = os.listdir ()

    # printing files and directories at "/bin"
    print (f'list of files and directories at "{dir_target}":')
    # for each file (or directory) in the list
    for filename in list_files:
        # printing name of file (or directory)
        print (f'  {filename}')

# execution of main function
if (__name__ == '__main__'):
    main ()
