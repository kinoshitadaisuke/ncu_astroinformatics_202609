#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:26:55 (UT+08:00) daisuke>
#

# importing os module
import os

# main function
def main ():
    # target file
    file_target = '/etc/fstab'

    # file information
    stat = os.stat (file_target)

    # printing file information
    print (f'status of file "{file_target}":')
    print (f'  file owner UID  = {stat.st_uid}')
    print (f'  file owner GID  = {stat.st_gid}')
    print (f'  file mode       = {oct (stat.st_mode)}')
    print (f'  file size       = {stat.st_size} byte')
    print (f'  number of links = {stat.st_nlink}')

# execution of main function
if (__name__ == '__main__'):
    main ()
