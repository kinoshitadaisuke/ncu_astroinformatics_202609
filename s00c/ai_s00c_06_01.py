#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:49:47 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# main function
def main ():
    # command to be executed
    command = 'uname -srm'

    # executing a command "uname" and capturing output
    result = subprocess.run (command, shell=True, capture_output=True)

    # stdout of command execution
    output = result.stdout.decode ('utf-8')

    # printing result of command execution
    print (f'Outputs from the execution of command "{command}":')
    print (f'{output}')

# execution of main function
if (__name__ == '__main__'):
    main ()
