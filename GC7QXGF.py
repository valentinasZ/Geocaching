from PIL import Image

im = Image.open('Océan.bmp')
pix = im.load()
width, height = im.size
p_oints=[(141,182),(537,1205),(820,1271),(1262,1027),(96,1074),(1109,960),(295,1677),(1202,1122),(858,1422),
(427,1351),(1247,1332),(664,1747),(358,1420),(267,741),(680,1889),(623,197),(420,1847),(1072,474),(706,805),
(529,1032),(1195,1859),(306,1005),(478,999),(1035,1471),(505,1207),(1019,1221),(992,403),(1056,1324),
(816,1629),(477,346),(92,336),(453,760),(1014,1127),(1132,1903),(1136,1649),(199,1231),(1146,917),(480,809),(1231,339),(556,1261),(560,937),(266,542),(201,711),(909,682)]
c = []
for a, b in p_oints:
    RGB = im.getpixel((b, a))
    R, G, B = RGB
    c.append(bin(B)[-3]+bin(B)[-2])
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