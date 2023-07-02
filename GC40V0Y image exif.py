#pip3 install piexif
#pip3 install gpsphoto
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
from GPSPhoto import gpsphoto
import exifread



def GC40V0Y(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    description = str(soup.find('img', alt='Uzdevums'))
    img = description.split('"')[-2]
    urllib.request.urlretrieve(img,'image.jpg')
    pic = Image.open("image.jpg")
    exifdata = pic.getexif()

    #for exif data
    for tag_id in exifdata:
        tag = TAGS.get(tag_id,tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

    # for gps in the  exif
    gps = gpsphoto.getGPSData("image.jpg")
    return gps['Latitude'],gps['Longitude']









result = GC40V0Y('https://www.geocaching.com/geocache/GC40V0Y_lv127')
print(result)