#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:33:43 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# main function
def main ():
    # URL of GitHub repository
    url_repo = 'https://github.com/architecture-building-systems/honey-badger.git'

    # command for downloading GitHub repository
    command_git = f'git clone {url_repo}'

    # downloading GitHub repository
    subprocess.run (command_git, shell=True)

# execution of main function
if (__name__ == '__main__'):
    main ()
