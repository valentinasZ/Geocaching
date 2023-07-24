import requests
from bs4 import BeautifulSoup
import re
from textwrap import wrap
def GC2K6EQ(url):
    binary = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    text = str(soup.find('span',id="ctl00_ContentBody_LongDescription"))
    for match in re.finditer(r'<font color="(green|purple)">(.*?)</font>', text):
        if match.group(1) == 'green':
            binary+='0'
        else:
            binary+='1'
    for i in wrap(binary,8):
        decimal_value = int(i, 2)
        ascii_character = chr(decimal_value)
        print(ascii_character, end='')
        #Imagine by John Lennon                N 20 36.249 W 100 22.702







result = GC2K6EQ('https://coord.info/GC2K6EQ')
