import sys
import math
import timeit
from collections import Counter
import random
from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence
import numpy as np

# run code: python3 main.py < input.txt

# input format:
# plaintext 
# keyCaesar 
# keyRail-fence

def caesarAlogirhm():
    print('Encode with Caesar Cipher:')
    _caesarCipher = Caesar(alphabet, keyCaesar)
    ciphertext = _caesarCipher.encrypt(plaintext)
    print('ciphertext = ', ciphertext)
    print()
    print('Decode with Caesar Cipher:')
    list_keyCaesar = np.random.permutation(len(alphabet))

    for key in list_keyCaesar:
        _caesarCipher.setKey(key)
        temp_plaintext = _caesarCipher.decrypt(ciphertext)
        if (temp_plaintext == plaintext):
            print('plaintext = ', plaintext)
            print('key = ', key)
            return
        
    assert False, 'error with decode in caesarAlgorithm'

def Rail_fenceAlgorithm():
    print('Encode with Rail Fence Cipher:')
    _rail_fenceCipher = Rail_fence(keyRail_fence)
    ciphertext = _rail_fenceCipher.encrypt(plaintext)
    print('ciphertext = ', ciphertext)
    print()
    print('Decode with Rail Fence Cipher:')

    list_keyRail_fence = [key for key in range(2, len(ciphertext))]
    random.shuffle(list_keyRail_fence)

    for key in list_keyRail_fence:
        _rail_fenceCipher.setKey(key)
        temp_plaintext = _rail_fenceCipher.decrypt(ciphertext)
        if (temp_plaintext == plaintext):
            print('plaintext = ', plaintext)
            print('key = ', key)
            return
        
    assert False, 'error with decode in Rail_fenceAlgorithm'


start = timeit.default_timer()

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
plaintext = input()
keyCaesar = int(input())
keyRail_fence = int(input())

print("Plaintext Input =", plaintext)
print()
if True:
    begin = timeit.default_timer()
    
    caesarAlogirhm()

    end = timeit.default_timer()

    print('Time Caesar Cipher = ', end - begin)
    print()

if True:
    begin = timeit.default_timer()
    
    Rail_fenceAlgorithm()
    
    end = timeit.default_timer()
    print('Time Rail Fence Cipher = ', end - begin)
    
stop = timeit.default_timer()
print('Time: ', stop - start, file = sys.stderr)