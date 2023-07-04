import requests
from bs4 import BeautifulSoup
import base64
#task decode base64 message
def GC541EY(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    text = str(soup.find('span',id='ctl00_ContentBody_ShortDescription'))
    index = text.index(':')
    task = text[index+1:] #NTUuMDQxODU5LCAyNS4zNjcwNDM=
    return base64.b64decode(task) #b'55.041859, 25.367043'
result = GC541EY('https://www.geocaching.com/geocache/GC541EY_drasiai-challenge')
print(result)