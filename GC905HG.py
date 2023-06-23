# task
#2b3697db6c40d956b634bb4808a123ba

#Format for needed hash text: HDD MM.mmm HDDD MM.mmm

#For example N59 20.110 E024 44.920 MD5 hash is 3200523761f00a12300324383a5bf95e

from itertools import product
import hashlib

#test
coords = 'N59 20.110 E024 44.920'
hash =hashlib.md5(coords.encode()).hexdigest()
if hash == '3200523761f00a12300324383a5bf95e':
    print(coords,True)
else:
    print(False)

#project final coordiantes must be closer than 3.1km from start coordiantes
# we certainly know start N59 after could be 1 or 2 anfter we certailny know E024 4
digits = '0123456789'
for combo in product(digits, repeat = 9):
    coords = "N59 2{}.{} E024 4{}.{}".format(
        ''.join(combo[1:2]), ''.join(combo[2:5]), ''.join(combo[5:6]), ''.join(combo[6:9]))
    hash = hashlib.md5(coords.encode()).hexdigest()
    if hash == '2b3697db6c40d956b634bb4808a123ba':
        print(coords)
        break
    else:
        print(coords + '  WRONG')

    # answer N59 21.216 E024 46.157
