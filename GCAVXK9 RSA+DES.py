# # task:
# The coded message is encrypted with triple-DES in electronic code book mode.It uses a 128-bit EDE key.
# The RSA public key cryptosystem has been used to encipher the triple-DES key.
# we have the public exponent e and  public modulus n
# Firstly we need to find p and q two primes numbers p*q = n
# I am going to use Pollard’s Rho Algorithm for Prime Factorization which is in primefac module


import primefac
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from Crypto.Cipher import DES
import base64


def primes_finder(n):
    pass
    # factors = list(primefac.primefac(n))
    # return factors
    # it takes a while to fin p and q and we pretend that we know p and q values

def private_exponent(p,q,e):
    phi = (p-1)*(q-1)
    d = inverse(e,phi)
    return d

def RSA_private_key(n, e, d,p,q):

    private_key = RSA.construct((n, e, d, p, q))
    return private_key

def Decoding_DES_key(hex_message,private_key):
    key = hex(pow(int(hex_message, 16),private_key.d,private_key.n)).upper()[2:]
    return key[:int(len(key)/2)]

def des_decoding(Des_message,des_keyword):
    des = DES.new(bytes.fromhex(des_keyword), DES.MODE_ECB)
    ciphertext = base64.b64decode(Des_message)
    return des.decrypt(ciphertext)



if __name__ == "__main__":

    n = 82677476310335936967541680675025737883695845263553005931985128739041212937501943006371647950578739335611
    p = 25735210038873214106468352000040000556033567863435759
    q = 3212621003887321410646835200007003005560335677405429
    e = 32477443143064571502473601057877449384436429737570364401401588355509942198787392056535628395806452913649
    hex_message = "F1A4A49BF3589C179C664AAB39942B830965D9F7CC150D004680684982798A5CC3305CD71F08FD25DB7309"
    Des_message = 'T+DY2FMCBTweYLb6piApSgshc4m8Vb7HhvdgaI5i5tDCYp+0HSfic9VzFW+Kv8bbnMvtCatn7XFVlitcaDLPSZGqrFcICdqeO/VdNivKkrm6T6q2WL8082+gmRPGCNjbqdiXwYzrV8ahXo/R+bXkuOBtAQLQUFMOeGZrQDAalzY3ntho7itmzqRFGEsgP264DuFITRYwACkI5322CaUFdYNRmA/2CHCs1DrSIxdWifQ8KhLHlWx8H23TRe1x6zOp/fTYvIRCG8I54EvoFt6tmHPd9/g4jyWRL0v+n9DUFmi6StGyZMwA8Kbfwzyia5GU3jnv6txeBv6Ozlh9+OGFSyqZx99A1fodlyPo/d0QWzYaEQleXLyZ5lEEiwHn3CsywQZFrkbik7D1xu9JFmuv6g=='
    d = private_exponent(p, q, e)
    private_key = RSA_private_key(n, e, d, p, q)

    print("Private Exponent (d):", d)
    print("Private Key:", private_key)

    des_key = Decoding_DES_key(hex_message, private_key)
    print("Decoded DES Key:", des_key)

    decrypted_message = des_decoding(Des_message, des_key)
    print("Decrypted Message:", decrypted_message.decode())





