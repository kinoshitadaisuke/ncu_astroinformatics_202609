#!/usr/bin/env python3

#
# Time-stamp: <2026/09/01 10:52:00 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# main function
def main ():
    # timezone information (UT+0)
    tzinfo = datetime.timezone (datetime.timedelta (0.0), name='UT+0')

    # current time in UTC
    time_now_utc = datetime.datetime.now (tz=tzinfo)

    # printing result
    print (f'current time in UTC = {time_now_utc}')

# execution of main function
if (__name__ == '__main__'):
    main ()
