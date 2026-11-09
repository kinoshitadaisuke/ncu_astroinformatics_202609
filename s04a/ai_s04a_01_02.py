#!/usr/bin/env python3

#
# Time-stamp: <2026/11/09 10:38:28 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# main function
def main ():
    # target name
    target = 'Sun'

    # observatory (D35 ==> Lulin Observatory)
    #
    # To get a list of available observatory codes, visit following web page.
    #   https://www.minorplanetcenter.net/iau/lists/ObsCodes.html
    #
    obs_site = 'D35'

    # date/time
    t  = astropy.time.Time ('2026-07-01T04:00:00', scale='utc', format='isot')
    jd = t.jd

    # sending a query to NASA/JPL Horizons system
    obj = astroquery.jplhorizons.Horizons (id_type=None, id=target, \
                                           location=obs_site, epochs=jd)

    # getting ephemerides
    ephemerides = obj.ephemerides ()

    # printing ephemerides
    print (ephemerides.info)

# executing main function
if (__name__ == '__main__'):
    main ()
