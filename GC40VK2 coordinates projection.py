#basic coordinates = N 56° 17.449 E 024° 34.602
#task projection 709m 255.2°
import requests
from bs4 import BeautifulSoup
import geopy
import geopy.distance
import re
import pycaching


def GC40VK2(url):
    geocaching = pycaching.login('username', 'password')
    value = url.split('/')[-1][:7]
    print(value)
    cache = geocaching.get_cache(value)
    cache.load_quick()
    loc = (cache.location) #56 17m 26.952s N, 24 34m 36.12s E)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    description = str(soup.find('span', id='ctl00_ContentBody_LongDescription'))

    distance = float(''.join(re.findall(r'(\d+)m',description,re.DOTALL)))
    angle = float(''.join(re.findall(r'(\d+.\d+)°',description,re.DOTALL)))

    destination_point = geopy.distance.distance(meters=distance).destination((loc[0], loc[1]), bearing=angle)
    return destination_point.format_unicode()




result = GC40VK2('https://www.geocaching.com/geocache/GC40VK2_lv129') #https://www.geocaching.com/geocache/GC40VK2_lv129
print(result) #56° 17′ 21.0947″ N, 24° 33′ 56.2705″ E

