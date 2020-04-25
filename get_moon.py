import astropy
from astropy.coordinates import get_moon
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
mypos = EarthLocation(lat=33.979*u.deg, lon=-117.339*u.deg, height=310*u.m)
utcoffset = -7*u.hour
time = Time.now() - utcoffset
print(get_moon(time, mypos))
