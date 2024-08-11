# task: You have 3 seconds to scan the QR code, and submit the message. If you're fast enough, the server will give you the Flag.
# (And before you ask, yes the Qr code is malformed. Find a way to rebuild it, scan it and submit the message fast enough.)
# https://wawawoom.fr/geocaching/GC8GG1R/step4-4d0e43ca-56de-465b-8fac-6ce35429502f/


from PIL import Image
from pyzbar.pyzbar import decode
import requests
from bs4 import BeautifulSoup
import os
from io import BytesIO
import re
import time


def getdata(url,base_url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    img_tag = str(soup.find('img', id="qr-image"))
    img_src = re.search(r'src="([^"]*)"', img_tag).group(1)

    image_url = os.path.join(base_url, img_src)
    response = requests.get(image_url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        return None

def make_white_transparent(base_image,qr_image):
    qr_image = qr_image.convert("RGBA")
    base_image = base_image.convert("RGBA")

    datas = qr_image.getdata()
    new_data = [(255, 255, 255, 0) if item[:3] == (255, 255, 255) else item for item in datas]
    qr_image.putdata(new_data)

    qr_image = qr_image.resize(base_image.size)
    merged_image = Image.alpha_composite(base_image, qr_image)
    return merged_image


def scan_qr(image):
    decoded_data = decode(image)
    return decoded_data[0].data.decode('utf-8') if decoded_data else None


def post_data(decoded_message, html):
    data = {
        "qr" : decoded_message,
        "submit": "Submit",
    }
    response = requests.post(html, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    flag_div = soup.find('div', class_="right-col-content")

    if flag_div:
        flag_span = flag_div.find('span', class_="badge badge-light text-monospace")
        if flag_span:
            return flag_span.get_text(strip=True)



def main():
    start_time = time.time()

    qr_image = getdata('https://wawawoom.fr/geocaching/GC8GG1R/step4-4d0e43ca-56de-465b-8fac-6ce35429502f/','https://wawawoom.fr/geocaching/GC8GG1R/')
    base_image = Image.open('0d29dbd1.png')

    merged_image = make_white_transparent(base_image, qr_image)
    decoded_message = scan_qr(merged_image)


    response_text = post_data(decoded_message,'https://wawawoom.fr/geocaching/GC8GG1R/step4-4d0e43ca-56de-465b-8fac-6ce35429502f/')
    print(f"My flag is: {response_text}")



    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

main()


