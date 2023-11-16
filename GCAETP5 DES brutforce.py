from Crypto.Cipher import DES
from itertools import product


for keyGen in product(range(0, 256, 2), repeat=4):
            key = bytearray((19, 52, 87, 220, keyGen[0], keyGen[1],keyGen[2],keyGen[3]))
            cipher = DES.new(key, DES.MODE_ECB)
            ciphertext = cipher.decrypt(bytes.fromhex('3648117E9C1DC7E4AFAF91B223C004E07436E75B53C9A8FC243BA8FB77D537DA64F56604FC6C933028E967976E37E414DB7815269EBC8C31FBC2821D97B9D1229DEBA764F83314DEF481A372CF12F27604DDEE254F062589EC5882C08ED712F8D042471CEE14CBD31DC77E1FCC866048'))
            print( keyGen[0], keyGen[1],keyGen[2],keyGen[3])
            try:
                plaintext = ciphertext.decode('utf-8')
                print(plaintext)
                with open('failas.txt.txt', 'a') as myfile:
                    for line in plaintext:
                        myfile.writelines(plaintext +' key: '+str([keyGen[0],keyGen[1],keyGen[2],keyGen[3]])+'\n')
                        myfile.flush()
                        break
            except:
                continue

