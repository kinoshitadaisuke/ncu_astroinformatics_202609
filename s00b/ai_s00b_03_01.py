#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:28:16 (UT+08:00) daisuke>
#

# defining a function to add two numbers
def add_two_numbers (a, b):
    # adding two numbers
    c = a + b
    # returning result of calculation
    return (c)

# main function
def main ():
    # two numbers
    n1 = 23
    n2 = 47

    # using the function "add_two_numbers"
    n3 = add_two_numbers (n1, n2)

    # printing result
    print (f'n1 = {n1}')
    print (f'n2 = {n2}')
    print (f'n3 = n1 + n2 = {n3}')

# execution of main function
if (__name__ == '__main__'):
    main ()
