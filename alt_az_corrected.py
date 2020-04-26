
import matplotlib.pyplot as plt
import numpy as np
from astropy.visualization import astropy_mpl_style, quantity_support 
plt.style.use(astropy_mpl_style)
quantity_support()


import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

m13 = SkyCoord.from_name('M13')
toronto = EarthLocation(lat=43.6532*u.deg, lon=-79.3832*u.deg, height=209*u.m)
utcoffset = -4*u.hour  # Eastern Daylight Time
time = Time('2020-4-25 23:37:00') - utcoffset
m13altaz = m13.transform_to(AltAz(obstime=time,location=toronto))

print(m13altaz)