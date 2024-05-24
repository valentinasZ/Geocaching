import requests
from bs4 import BeautifulSoup
import re
from base64 import b64decode
import PyPDF2

def decoding_base_64(URL):

  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find("span",id="ctl00_ContentBody_LongDescription")
  b64 = results.text
  b64 = ''.join(b64)
  b_64 = re.sub(r'[\r\n]', '', b64)

  bytes = b64decode(b_64,validate=True)
  if bytes[0:4] != b'%PDF':
    raise ValueError('Missing the PDF file signature')

  f = open('file.pdf', 'wb')
  f.write(bytes)
  f.close()


decoding_base_64("https://www.geocaching.com/geocache/GC3P287_crack-it")

def open_pdf(pdf_path):
  file = PyPDF2.PdfReader(pdf_path)
  out = PyPDF2.PdfWriter()
  if file.is_encrypted:
    for i in range(1,9999):
      file.decrypt(str(i))
  for page in file.pages:
    out.add_page(page)

  with open(pdf_path, "wb") as f:
    out.write(f)

  print(out)

open_pdf('file.pdf')



