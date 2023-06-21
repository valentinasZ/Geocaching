# after you solve puzzle
# Task:
# N 54 IFVMTGEJZ
# E 25 WGHSFEUTO
from textwrap import wrap
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
MORSE_TO_DIGIS = {'.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0'

}
def Puzlius_2(task):
    temp = ''
    decoded = ''
    for letter in task:
        temp+=MORSE_CODE_DICT[letter]

    morse = wrap(temp,5)
    for i in morse:
        decoded+=MORSE_TO_DIGIS[i]
    return 'N 54.{} E 25.{}'.format(decoded[:5],decoded[5:])





result = Puzlius_2('IFVMTGEJZWGHSFEUTO')
print(result)


