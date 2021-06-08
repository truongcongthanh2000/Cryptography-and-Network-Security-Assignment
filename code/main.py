import sys
import math
import timeit
from collections import Counter
import random
from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence
from encrypt import Encrypt
from decrypt_withscore import Decrypt_withscore
from decrypt_withEngDic import Decrypt_withEngDic
from decrypt_withcharacter_phrase import Decrypt_withcharacter_phrase
import numpy as np

# run code: python3 main.py < input.txt

# input format:
# plaintext 
# keyCaesar 
# keyRail-fence

def caesarAlogirhm():
    print('Encode with Caesar Cipher:')
    ciphertext = list_ciphertext[0]
    print('ciphertext = ', ciphertext)
    print()
    begin = timeit.default_timer()

    print('Decode with Caesar Cipher with Letter Frequency:')

    print(_decrypt_withsLetter_Frequency.decrypt_caesar(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Caesar Cipher with Letter Frequency =', end - begin)

    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Caesar Cipher with Character Phrase:')

    print(_decrypt_withCharacter_Phrase.decrypt_caesar(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Caesar Cipher with Character Phrase =', end - begin)
    
    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Caesar Cipher with English Dictionary:')
    print(_decrypt_withEngDic.decrypt_caesar(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Caesar Cipher with English Dictionary =', end - begin)
    print()


def Rail_fenceAlgorithm():
    print('Encode with Rail Fence Cipher:')
    ciphertext = list_ciphertext[1]
    print('ciphertext = ', ciphertext)
    print()
    begin = timeit.default_timer()

    print('Decode with Rail_fence Cipher with Letter Frequency:')

    print(_decrypt_withsLetter_Frequency.decrypt_Rail_fence(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence Cipher with Letter Frequency =', end - begin)
    
    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Rail_fence Cipher with Character Phrase:')

    print(_decrypt_withCharacter_Phrase.decrypt_Rail_fence(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence Cipher with Character Phrase =', end - begin)
    
    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Rail_fence Cipher with English Dictionary:')
    print(_decrypt_withEngDic.decrypt_Rail_fence(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence Cipher with English Dictionary =', end - begin)
    print()

# Rail_fence(Caesar())
def productAlgorithm():
    print('Encode with product encryption Rail_fence x Caesar')
    ciphertext = list_ciphertext[2]
    print('ciphertext = ', ciphertext)
    print()

    begin = timeit.default_timer()

    print('Decode with Rail_fence x Caesar Cipher with Letter Frequency:')

    print(_decrypt_withsLetter_Frequency.decrypt_Product(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence x Caesar Cipher with Letter Frequency =', end - begin)

    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Rail_fence x Caesar Cipher Cipher with Character Phrase:')

    print(_decrypt_withCharacter_Phrase.decrypt_Product(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence x Caesar Cipher with Character Phrase =', end - begin)
    
    print()

    # ----------------------------------------------------

    begin = timeit.default_timer()

    print('Decode with Rail_fence x Caesar Cipher with English Dictionary:')
    print(_decrypt_withEngDic.decrypt_Product(ciphertext))

    end = timeit.default_timer()

    print('Time execute Decode with Rail_fence x Caesar Cipher with English Dictionary =', end - begin)
    print()


start = timeit.default_timer()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
print(len(alphabet))
plaintext = input()
keyCaesar = int(input())
keyRail_fence = int(input())

print("Plaintext Input =", plaintext)
print("keyCaesar Input =", keyCaesar)
print("keyRail_fence Input =", keyRail_fence)
print()

_encrypt = Encrypt(alphabet, keyCaesar, keyRail_fence)

# [Caesar, Rail_fence, Rail_fence(Caesar)]
list_ciphertext = _encrypt.encrypt(plaintext)
# print("List ciphertext = ")
# for x in list_ciphertext:
#     print(x)
_decrypt_withsLetter_Frequency = Decrypt_withscore(alphabet)
_decrypt_withEngDic = Decrypt_withEngDic(alphabet)
_decrypt_withCharacter_Phrase = Decrypt_withcharacter_phrase(alphabet)


if True:
    begin = timeit.default_timer()
    
    print('--------------------------------------------------------------------------------------')
    caesarAlogirhm()

    end = timeit.default_timer()

    print('Time Caesar Cipher = ', end - begin)
    print()

if True:
    begin = timeit.default_timer()
    
    print('--------------------------------------------------------------------------------------')

    Rail_fenceAlgorithm()
    
    end = timeit.default_timer()
    print('Time Rail Fence Cipher = ', end - begin)
    print()

if True:
    begin = timeit.default_timer()
    
    print('--------------------------------------------------------------------------------------')
   
    productAlgorithm()
    
    end = timeit.default_timer()
    print('Time Rail Rail_fence x Caesar Cipher = ', end - begin)


stop = timeit.default_timer()
print('Time: ', stop - start, file = sys.stderr)