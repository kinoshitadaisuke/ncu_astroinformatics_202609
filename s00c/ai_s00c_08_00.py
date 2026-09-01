#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:51:06 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# main function
def main ():
    # time offset from UTC
    #   local time in Taiwan = UT + 8-hr
    dt = datetime.timedelta (hours=8)

    # current time in local time
    time_now_local = datetime.datetime.now (tz=datetime.timezone (dt))

    # printing result
    print (f'current local time: {time_now_local}')

# execution of main function
if (__name__ == '__main__'):
    main ()
