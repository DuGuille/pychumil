import math
import datetime

gt_lat = 14.613
gt_lon = -90.535

def ra2real( hr, min =0):
    """convert right ascension (hours, minutes) to degrees as real
    
    Ported from the code by Stephen R. Schmitt at http://mysite.verizon.net/res148h4j/javascript/script_celestial2horizon.html
    """
    return 15.0*(hr + min/60.0)

def coord_to_horizon(ra, dec, lat, lon, meansideraltime ):
    """Compute horizon coordinates from ra, dec, lat, lon, and utc
    
    ra, dec, lat, lon in  degrees
    utc is a Date object
    results returned in hrz_altitude, hrz_azimuth
    
    Ported from the code by Stephen R. Schmitt at http://mysite.verizon.net/res148h4j/javascript/script_celestial2horizon.html
    """
    ha = meansideraltime - ra;
    if (ha < 0.0):
        ha = ha + 360.0

    # convert degrees to radians
    ha  = ha*math.pi/180.0
    dec = dec*math.pi/180.0
    lat = lat*math.pi/180.0

    # compute altitude in radians
    sin_alt = math.sin(dec)*math.sin(lat) + math.cos(dec)*math.cos(lat)*math.cos(ha)
    alt = math.asin(sin_alt)
    
    # compute azimuth in radians
    # divide by zero error at poles or if alt = 90 deg
    cos_az = (math.sin(dec) - math.sin(alt)*math.sin(lat))/(math.cos(alt)*math.cos(lat))
    az  = math.acos(cos_az)

    # convert radians to degrees
    hrz_altitude = alt*180.0/math.pi;
    hrz_azimuth  = az*180.0/math.pi;

    # choose hemisphere
    if (math.sin(ha) > 0.0):
      hrz_azimuth = 360.0 - hrz_azimuth;
    
    return (hrz_altitude, hrz_azimuth)



def mean_sidereal_time(now, lon):
    """Compute the Mean Sidereal Time in units of degrees.
    
    Use lon := 0 to get the Greenwich MST.
    East longitudes are positive; West longitudes are negative
    returns: time in degrees
    
    Ported from the code by Stephen R. Schmitt at http://mysite.verizon.net/res148h4j/javascript/script_celestial2horizon.html
    """
    year = now.year
    month = now.month
    hour = now.hour
    minute = now.minute
    second = now.second
    day = now.day
    
    if ((now.month == 1) or (now.month == 2)):
        year  = year - 1
        month = month + 12

    a = math.floor(year/100.0)
    b = 2.0 - a + math.floor(a/4.0)
    c = math.floor(365.25*year)
    d = math.floor(30.6001*(month + 1.0))

    # days since J2000.0
    jd = b + c + d - 730550.5 + day + (hour + minute/60.0 + second/3600.0)/24.0
    
    # julian centuries since J2000.0
    jt = jd/36525.0

    # the mean sidereal time in degrees
    mst = 280.46061837 + 360.98564736629*jd + 0.000387933*jt*jt - jt*jt*jt/38710000.0 + lon

    # in degrees modulo 360.0
    if (mst > 0.0):
        while (mst > 360.0):
          mst = mst - 360.0
    else:
        while (mst < 0.0):
          mst = mst + 360.0
        
    return mst

def get_brightest_hyg(lat, lon, nstars=20, filename='hygfull.csv', utc = None):
    file = open(filename, 'r')
    stars = []
    if utc is None:
        utc = datetime.datetime.utcnow();
    mst = mean_sidereal_time( utc, lon )
    # skip 1 line
    file.readline()
    for line in file:
        csvalues = line.split(',')
        try:
            ra = float(csvalues[7])
            dec = float(csvalues[8])
            mag = float(csvalues[10])
            if (mag > 5.0):
                continue
            alt,az = coord_to_horizon(ra2real(ra), dec, lat, lon, mst)
            
            # if star is above horizon, append it
            if (alt > 0):
                stars.append(
                  {
                    'id': csvalues[0],
                    'bayerflamsteed': csvalues[5],
                    'hdraper_id': csvalues[1],
                    'harvard_rev_id': csvalues[2],
                    'mag': mag,
                    'ra': ra,
                    'dec': dec,
                    'altitude': alt,
                    'azimuth': az,
                    'name': csvalues[6],
                    'gliesse': csvalues[4]
                  })
        except:
            print csvalues
    file.close()

    stars.sort(key= lambda x : x['mag'], reverse = False )
    return stars[0:nstars]
    
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('lat', help='latitude (default is Guatemala city latitude)', default = gt_lat, nargs='?', type=float)
    parser.add_argument('lon', help='longitude (default is Guatemala city longitude)', default = gt_lon, nargs='?', type=float)
    args = parser.parse_args()
    print 'UTC:%s, lat: %f, lon: %f' % (str(datetime.datetime.utcnow()), args.lat, args.lon)
    for star in get_brightest_hyg(args.lat, args.lon):
     print '%s (Gliesse %s)  (BayerFlamsteed %s) Magnitud=%f\n\t\t  [Altitud %f, Azimuth %f ] ' %  (star['name'], star['gliesse'], star['bayerflamsteed'], star['mag'], star['altitude'], star['azimuth'])