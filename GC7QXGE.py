from PIL import Image

im = Image.open('Hot.dib')
pix = im.load()
width, height = im.size
p_oints= [(25,443),(115,421),(181,168),(168,235),(84,156),(119,404),(137,449),(153,455),(32,289),(197,95),(178,620),(162,132),(56,502),(189,431),(41,374),(35,211),(143,227),(60,476),(102,339),(224,330),(20,41),(116,272),(88,294),(161,201),(184,355),(204,268),(217,555),(123,212),(151,398),(95,193),(39,47),(44,171),(99,413),(48,396),(69,333),(214,514)]
c = []
for a, b in p_oints:
    RGB = im.getpixel((b, a))
    R, G, B = RGB
    c.append(bin(R)[-2:])
binary_int = int(''.join(c), 2)
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
# Converting the array into ASCII text
ascii_text = binary_array.decode('utf-8')
# Getting the ASCII value
print(ascii_text)
# write code to the geocheker


