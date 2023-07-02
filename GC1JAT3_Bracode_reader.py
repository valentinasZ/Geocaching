from pyzbar.pyzbar import decode
import cv2 #opencv-python
def GC1JAT3(path):
    #save iamge with barcode from the log
    code_image = cv2.imread(path)
    cv2.imshow("QR", code_image)
    decoded = decode(code_image)
    return decoded #N54 40.546 E25 14.227




result = GC1JAT3('barcode.jpg')
print(result)