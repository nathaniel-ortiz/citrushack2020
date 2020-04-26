import json
import astropy
from astropy.coordinates import get_moon
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, GCRS, solar_system_ephemeris, ICRS, Angle, Latitude, Longitude
from astropy.utils.misc import JsonCustomEncoder

mypos = EarthLocation(lat=33.979*u.deg, lon=-117.339*u.deg, height=1014*u.m)
utcoffset = -7*u.hour
time = Time.now() + utcoffset
solar_system_ephemeris.set('jpl')
m13 = SkyCoord.from_name('M13')
m13_AltAz = m13.transform_to(AltAz(obstime=time, location=mypos))

#with solar_system_ephemeris.set('jpl'):
m13_GCRS = m13.transform_to(GCRS(obstime=time))

moon_GCRS = get_moon(time, mypos)
moon_AltAz = moon_GCRS.transform_to(AltAz(obstime=time, location=mypos))
print(moon_GCRS)
print(moon_AltAz.to_string(style='hmsdms'))
print(m13_GCRS)
print(m13_AltAz)
