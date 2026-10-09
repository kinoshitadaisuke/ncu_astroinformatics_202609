#!/usr/bin/env python3

#
# Time-stamp: <2026/09/30 10:42:48 (UT+08:00) daisuke>
#

# importing astroquery module
import astroquery.mast

# main function
def main ():
    # making mast object
    mast = astroquery.mast.Mast ()

    # target object name
    object_name = 'M1'

    # choice of name resolver
    name_resolver = 'SIMBAD'

    # coordinates
    coords = mast.resolve_object (object_name, resolver=name_resolver)

    # RA and Dec of the object
    (ra, dec) = coords.to_string (style='hmsdms').split ()
    
    # printing object name and coordinates
    print (f'#')
    print (f'# result from name resolver')
    print (f'#')
    print (f'{object_name}')
    print (f'  RA  : {ra} = {coords.ra.deg} [deg]')
    print (f'  Dec : {dec} = {coords.dec.deg} [deg]')

# executing main function
if (__name__ == '__main__'):
    main ()
