import requests
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageDraw
def GC1W87X(url):
    tuples = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    text = str(soup.find('td',nowrap="nowrap"))
    for line in text.splitlines():
        match = re.findall(r'(\d+),(\d+),(\d+),(\d+)', line)
        for i in match:
            if i!=None:
                tuples.append((int(i[0]),int(i[1]),int(i[2]),int(i[3])))
    return tuples

def draw_image():
    img = Image.new('RGB', (504, 232), color=(255, 255, 255)) #image size equal original image size from the page
    draw = ImageDraw.Draw(img)
    for a,b,c,d in result:
        draw.line((a, b, c, d), fill=(0, 0, 0))
    img.show()


result = GC1W87X('https://www.geocaching.com/geocache/GC1W87X_meaningless-link#clue')
res = draw_image()

