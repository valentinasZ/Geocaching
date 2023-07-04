import requests
from bs4 import BeautifulSoup
import re
def pi_value(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    text = soup.find('pre')
    pi = text.text.strip()
    value = ''
    for i in pi:
        if i.isdigit()==True or i=='.':
            value+=i
    return value

result = pi_value('http://www.cecm.sfu.ca/organics/papers/borwein/paper/html/local/bdigits.html')


def pi_GC8XQVT(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find('span', id='ctl00_ContentBody_LongDescription')
    text = text.text.strip()
    pi = ''.join(re.findall(r'= (.*)',text,re.DOTALL))
    value_1 = ''
    for i in pi:
        if i.isdigit() == True or i == '.':
            value_1+=i
    return value_1

result_1 =pi_GC8XQVT('https://www.geocaching.com/geocache/GC8XQVT_immanuel-kant')


def compare(a,b):
    a = a[:len(b)]
    diff = ''
    for i,j in zip(a,b):
        if i!=j:
            diff+=i
    return diff #54 18 589 22 18 2659
    #task is solved and we got right coordinates

cords = compare(result,result_1)
print(cords)