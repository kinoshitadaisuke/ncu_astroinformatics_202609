#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:51:43 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# main function
def main ():
    # current time in UTC
    time_now_utc = datetime.datetime.now (tz=datetime.timezone.utc)

    # printing result
    print (f'current time in UTC = {time_now_utc}')

# execution of main function
if (__name__ == '__main__'):
    main ()
