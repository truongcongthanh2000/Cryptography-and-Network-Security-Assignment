from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence
from read_english_dictionary import english_words
# from english_words import english_words_set
import re 

LIMITS = 50

class Decrypt_withEngDic:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def isEnglishWord(self, word):
        return word.lower() in english_words
    
    def get_english_score(self, words):
        words_with_nospecial = re.sub('[^a-zA-Z0-9\n]', ' ', words)
        score = 0
        for word in words_with_nospecial.split():
            score += self.isEnglishWord(word)

        return score
    
    # https://github.com/ricpacca/cryptopals/blob/master/S1C03.py (singlechar_xor_brute_force(ciphertext))
    def decrypt_caesar(self, ciphertext):
        _caesarCipher = Caesar(self.alphabet, 0)
        candidates = []
        for key_candidate in range(len(self.alphabet)):
            _caesarCipher.setKey(key_candidate)
            plaintext_candidate = _caesarCipher.decrypt(ciphertext)

        
            candidate_score = self.get_english_score(plaintext_candidate)
            result = {
                'key': key_candidate,
                'score': candidate_score,
                'plaintext': plaintext_candidate
            }

            candidates.append(result) 

        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]

    def decrypt_Rail_fence(self, ciphertext):
        _rail_fenceCipher = Rail_fence(0)
        candidates = []
        for key_candidate in range(2, LIMITS + 1):
            _rail_fenceCipher.setKey(key_candidate)
            plaintext_candidate = _rail_fenceCipher.decrypt(ciphertext)

            candidate_score = self.get_english_score(plaintext_candidate)
            result = {
                'key': key_candidate,
                'score': candidate_score,
                'plaintext': plaintext_candidate
            }

            candidates.append(result) 

        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]

    # Rail_fence(Caesar(plaintext))
    def decrypt_Product(self, ciphertext):
        _caesarCipher = Caesar(self.alphabet, 0)
        _rail_fenceCipher = Rail_fence(0)
        candidates = []

        for keyRail_fence_candidate in range(2, LIMITS + 1):
            _rail_fenceCipher.setKey(keyRail_fence_candidate) 
            plaintextRail_fence_candidate = _rail_fenceCipher.decrypt(ciphertext)
            for key_candidate in range(len(self.alphabet)):
                _caesarCipher.setKey(key_candidate)
                plaintext_candidate = _caesarCipher.decrypt(plaintextRail_fence_candidate)
    
                candidate_score = self.get_english_score(plaintext_candidate)
                result = {
                    'key': key_candidate,
                    'score': candidate_score,
                    'plaintext': plaintext_candidate
                }

                candidates.append(result) 

        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]