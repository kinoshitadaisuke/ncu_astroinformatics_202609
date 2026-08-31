#!/usr/bin/env python3

#
# Time-stamp: <2026/08/31 19:29:27 (UT+08:00) daisuke>
#

# main function
def main ():
    # initialisation of a tuple
    planet = ( 'Mercury', 'Venus', 'Earth', 'Mars', \
               'Jupiter', 'Saturn', 'Uranus', 'Neptune' )

    # type of "planet"
    print ("type of planet:", type (planet) )

    # printing the tuple "tuple_a"
    print ("planet:\n", planet)

    # counting number of elements in the tuple "planet"
    n = len (planet)

    # printing number of elements in the tuple "planet"
    print ("len (planet) =", n)

    # accessing to an element using index
    print ("planet[2]    =", planet[2])
    print ("planet[7]    =", planet[7])
    print ("planet[-3]   =", planet[-3])

    # accessing to elements using slicing
    print ("planet[2:5]  =", planet[2:5])
    print ("planet[:4]   =", planet[:4])
    print ("planet[6:]   =", planet[6:])

# execution of main function
if (__name__ == '__main__'):
    main ()
