from PIL import Image

im = Image.open('Rainbow.bmp')
pix = im.load()
width, height = im.size
p_oints =[(1044,338),(1066,1095),(793,829),(538,514),(939,1485),(127,1133),(155,648)
,(116,306),(944,756),(816,344),(268,811),(839,534),(703,224),(691,553),(1089,221),
(1127,831),(899,75),(893,118),(771,843),(570,443),(892,1067),(73,785),(692,958),
(828,170),(998,172),(148,778),(697,874),(719,803),(969,525),(128,1413),(1039,1387),
(923,1210),(762,1512),(387,949),(646,1466),(672,1528),(813,1407),(674,997),(786,102)
,(599,1406),(1090,500),(779,94),(80,401),(137,399),(345,676),(789,566),(1155,724),(299,468)]
c = []
hex_colors = []
for a, b in p_oints:
    RGB = im.getpixel((b, a))
    R, G, B = RGB
    c.append(bin(R)[-2] + bin(G)[-2]+bin(B)[-2])

binary_int = int(''.join(c).replace('b','0'), 2)
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
# Converting the array into ASCII text
ascii_text = binary_array.decode()
# Getting the ASCII value
print(ascii_text)
# write code to the geocheker