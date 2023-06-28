import requests
from bs4 import BeautifulSoup
import numpy
from matplotlib import pyplot
import re
def GC4W2X3(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    span_element = soup.find('span', id='ctl00_ContentBody_LongDescription')
    task = str(span_element)[105:-24]
    joined_task =''.join(([i for i in task if i!=' ']))

    small_x_numbers = re.findall(r'x(\d+)', joined_task)
    big_x_numbers = re.findall(r'X(\d+)', task)
    small_y_numbers = re.findall(r'y(\d+)', joined_task)
    big_y_numbers = re.findall(r'Y(\d+)', joined_task)

    x1 = numpy.r_[[int(i) for i in small_x_numbers]]
    x2 = numpy.r_[[int(i) for i in big_x_numbers]]
    y1 = numpy.r_[[int(i) for i in small_y_numbers]]
    y2 = numpy.r_[[int(i) for i in big_y_numbers]]
    pyplot.plot(x1, y1)
    pyplot.plot(y2, x2)
    pyplot.grid(True)
    pyplot.show()









result =   GC4W2X3('https://www.geocaching.com/geocache/GC4W2X3')
print(result) #after take graph and combine with OSM and get real place
