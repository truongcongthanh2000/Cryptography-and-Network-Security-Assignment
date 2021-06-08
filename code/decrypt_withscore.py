from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence

# http://www.macfreek.nl/memory/Letter_Distribution (Raw statistics)
# http://www.macfreek.nl/memory/images/EN-Letters.txt
CHARACTER_FREQ = {
    'a': 0.0653217, 'b': 0.0125881, 'c': 0.0223368, 'd': 0.0328292, 'e': 0.1026665, 'f': 0.0198307, 'g': 0.0162490,
    'h': 0.0497856, 'i': 0.0566844, 'j': 0.0009752, 'k': 0.0056096, 'l': 0.0337755, 'm': 0.0202656, 'n': 0.0571201,
    'o': 0.0615957, 'p': 0.0150432, 'q': 0.0008367, 'r': 0.0498790, 's': 0.0531700, 't': 0.0751699, 'u': 0.0227579,
    'v': 0.0079611, 'w': 0.0170389, 'x': 0.0014092, 'y': 0.0142766, 'z': 0.0005128, ' ': 0.1828846
}

LIMITS = 50

class Decrypt_withscore:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def get_english_score(self, words):
        score = 0
        for letter in words:
            letter_lower = letter.lower()
            if (letter_lower >= 'a' and letter_lower <= 'z') or (letter_lower == ' '):
                score += CHARACTER_FREQ.get(letter_lower, 0)
            # else:
            #     score += CHARACTER_FREQ.get('z', 0) # replace special character by 'z'
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
        for x in candidates:
            print(x)
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
                    'key': [keyRail_fence_candidate, key_candidate],
                    'score': candidate_score,
                    'plaintext': plaintext_candidate
                }

                candidates.append(result) 
                
        candidates.sort(key=lambda c: c['score'], reverse=True)
        # for x in candidates:
        #     print(x)
        return candidates[0]