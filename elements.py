import urllib2
import datetime

def get_picture(lon, lat, size="640x640", heading=0, fov=90, pitch=0, fname=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".png"):
    URL = "https://maps.googleapis.com/maps/api/streetview?location="+str(lon)+","+str(lat)+"&size="+size+"&heading="+str(heading)+"&fov="+str(fov)+"&pitch="+str(pitch)
    res = urllib2.urlopen(URL)
    img = open(fname, "wb")
    try:
        img.write(res.read())
    except Exception:
        print("Error")
    finally:
        img.close()
    return None

get_picture(35, 135)
