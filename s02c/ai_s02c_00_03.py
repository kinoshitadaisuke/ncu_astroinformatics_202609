#!/usr/bin/env python3

#
# Time-stamp: <2026/09/30 11:15:56 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing astroquery module
import astroquery.mast

# main function
def main ():
    # initialising a parser
    descr = 'finding coordinates of given target object names'
    parser = argparse.ArgumentParser (description=descr)

    # adding arguments
    parser.add_argument ('objects', nargs='+', help='target object names')

    # parsing arguments
    args = parser.parse_args ()

    # input parameters
    list_objects = args.objects
    
    # making mast object
    mast = astroquery.mast.Mast ()

    # choice of name resolver
    name_resolver = 'NED'

    # printing header
    print (f'#')
    print (f'# results from name resolver')
    print (f'#')
    
    # for each object, finding coordinates
    for object_name in list_objects:
        # coordinates
        coords = mast.resolve_object (object_name, resolver=name_resolver)

        # RA and Dec of the object
        (ra, dec) = coords.to_string (style='hmsdms').split ()
    
        # printing object name and coordinates
        print (f'{object_name}')
        print (f'  RA  : {ra} = {coords.ra.deg} [deg]')
        print (f'  Dec : {dec} = {coords.dec.deg} [deg]')

# executing main function
if (__name__ == '__main__'):
    main ()
