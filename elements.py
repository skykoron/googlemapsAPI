import urllib2


def get_picture(lon, lat, size="640x640", heading=0, fov=90, pitch=0):
    URL = "https://maps.googleapis.com/maps/api/streetview?location="+str(lon)+str(lat)+"&size="+size+"&heading="+str(heading)+"&fov="+str(fov)+"&pitch="+str(pitch)
    ret URL

get_picture(35, 135)

