#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:19:49 (UT+08:00) daisuke>
#

# main function
def main ():
    # two numbers
    a, b = 23, 7

    # calculation
    quotient  = a // b
    remainder = a % b

    # printing result of calculation
    print (f'a         = {a}')
    print (f'b         = {b}')
    print (f'quotient  = {quotient}')
    print (f'remainder = {remainder}')
    print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')

# execution of main function
if (__name__ == '__main__'):
    main ()
