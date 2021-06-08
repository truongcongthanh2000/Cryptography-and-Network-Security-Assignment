from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence
# from english_words import english_words_set

ONE_LETTERS = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
TWO_LETTERS = [
    'th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 
    'en', 'es', 'of' 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 
    'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've', 'ss', 'ee', 'tt', 'ff', 'll', 'mm', 'oo'
]
THREE_LETTERS = [
    'the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men'
]
FOUR_LETTERS = [
    'that', 'with', 'have', 'this', 'will', 'your', 'from', 
    'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time'
]

LIMITS = 50

class Decrypt_withcharacter_phrase:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def get_english_score(self, words):
        score = 0
        plaint_text = str.lower(words)
        # for i, letter in enumerate(ONE_LETTERS):
        #     _score += plaint_text.count(letter) * ((len(ONE_LETTERS) - i) / len(ONE_LETTERS)) / 4
        
        for i, list_words in enumerate([TWO_LETTERS, THREE_LETTERS, FOUR_LETTERS]):
            for word in list_words:
                score += plaint_text.count(word) * (i + 1) / 3
        
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