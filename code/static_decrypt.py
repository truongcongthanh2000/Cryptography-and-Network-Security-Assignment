import sys
import timeit
from read_english_dictionary import english_words
import random 
from decrypt_withscore import Decrypt_withscore
from decrypt_withEngDic import Decrypt_withEngDic
from decrypt_withcharacter_phrase import Decrypt_withcharacter_phrase
from encrypt import Encrypt

LIMITS = 50

def gen_plaintext(numWord):
    plaintext = ""
    for idx in range(numWord):
        word = random.choice(list_english_words)
        if idx > 0:
            plaintext += ' '
        plaintext += word
    return plaintext

def test_medium():
    numWord = 30
    plaintext = gen_plaintext(numWord)
    keyCaesar = random.randint(0, len(alphabet) - 1)
    keyRail_fence = random.randint(2, min(LIMITS, len(plaintext) - 1))
    _encrypt = Encrypt(alphabet, keyCaesar, keyRail_fence)

    # [Caesar, Rail_fence, Rail_fence(Caesar)]
    list_ciphertext = _encrypt.encrypt(plaintext)

    _decrypt_withscore = Decrypt_withscore(alphabet)
    _decrypt_withEngDic = Decrypt_withEngDic(alphabet)
    _decrypt_withCharacter_Phrase = Decrypt_withcharacter_phrase(alphabet)
    ans = []

    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withscore.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withscore.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withscore.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
    
    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withCharacter_Phrase.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withCharacter_Phrase.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withCharacter_Phrase.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withEngDic.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withEngDic.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withEngDic.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
    return ans
    
def test_large():
    numWord = 200
    plaintext = gen_plaintext(numWord)
    keyCaesar = random.randint(0, len(alphabet) - 1)
    keyRail_fence = random.randint(2, min(LIMITS, len(plaintext) - 1))
    _encrypt = Encrypt(alphabet, keyCaesar, keyRail_fence)

    # [Caesar, Rail_fence, Rail_fence(Caesar)]
    list_ciphertext = _encrypt.encrypt(plaintext)

    _decrypt_withscore = Decrypt_withscore(alphabet)
    _decrypt_withEngDic = Decrypt_withEngDic(alphabet)
    _decrypt_withCharacter_Phrase = Decrypt_withcharacter_phrase(alphabet)

    ans = []

    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withscore.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withscore.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withscore.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withCharacter_Phrase.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withCharacter_Phrase.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withCharacter_Phrase.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

    if True:
        ciphertext = list_ciphertext[0]
        candidate = _decrypt_withEngDic.decrypt_caesar(ciphertext)
        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
        
        ciphertext = list_ciphertext[1]
        candidate = _decrypt_withEngDic.decrypt_Rail_fence(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)

        ciphertext = list_ciphertext[2]
        candidate = _decrypt_withEngDic.decrypt_Product(ciphertext)

        if candidate["plaintext"] == plaintext:
            ans.append(1)
        else:
            ans.append(0)
    return ans

def static_medium():
    ans = [0 for i in range(9)]
    numTest = 50
    for idx in range(numTest):
        result = test_medium()
        for i in range(9):
            ans[i] += result[i]
    
    print("Decoding algorithm measurement test with 50 times, the number of english words each time is 30")
    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with Letter Frequency: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[0] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[1] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[2] / numTest))
    print("-------------------------------------------------------------------------------------------")

    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with Character Phrase: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[3] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[4] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[5] / numTest))
    print("-------------------------------------------------------------------------------------------")

    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with English Dictionary: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[6] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[7] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[8] / numTest))
    print("-------------------------------------------------------------------------------------------")


def static_large():
    ans = [0 for i in range(9)]
    numTest = 15
    for idx in range(numTest):
        result = test_large()
        for i in range(9):
            ans[i] += result[i]
    
    print("Decoding algorithm measurement test with 15 times, the number of english words each time is 200")
    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with Letter Frequency: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[0] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[1] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[2] / numTest))
    print("-------------------------------------------------------------------------------------------")

    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with Character Phrase: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[3] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[4] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[5] / numTest))
    print("-------------------------------------------------------------------------------------------")

    print("-------------------------------------------------------------------------------------------")
    print("Decrypt with English Dictionary: ")
    print("Probability of success in Caesar Cipher = {:.10f}".format(ans[6] / numTest))
    print("Probability of success in Rail_fence Cipher = {:.10f}".format(ans[7] / numTest))
    print("Probability of success in Rail_fence x Caesar Cipher = {:.10f}".format(ans[8] / numTest))
    print("-------------------------------------------------------------------------------------------")

start = timeit.default_timer()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
list_english_words = list(english_words)
static_medium()
print()
static_large()

stop = timeit.default_timer()
print('Time: ', stop - start, file = sys.stderr)




