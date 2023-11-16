from PIL import Image

im = Image.open('Forest.bmp')
pix = im.load()
width, height = im.size
p_oints= [(554,1051),(553,1005),(87,1095),(378,81),(320,994),(263,628),(306,660),(559,583),(122,232),(91,747),(503,652),(466,915),(77,719),(480,312),(549,195)
,(260,74),(363,367),(713,681),(714,324),(158,1096),(672,829),(388,55),(494,302),(483,545),(313,849),(418,913),(218,1019),(220,523),(467,213),(599,1014),(524,436),(664,340)]
c = []
for a, b in p_oints:
    RGB = im.getpixel((b, a))
    R, G, B = RGB
    c.append(bin(G)[-3]+bin(G)[-1])
binary_int = int(''.join(c), 2)
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
# Converting the array into ASCII text
ascii_text = binary_array.decode()
# Getting the ASCII value
print(ascii_text)
# write code to the geocheker
