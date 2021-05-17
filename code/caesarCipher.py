class Caesar:
    def __init__(self, alphabet = "", key = -1):
        self.setAlphabet(alphabet)
        self.setKey(key)
        assert key < len(alphabet), "key must be in range [0, len(alphabet))"
    
    def setAlphabet(self, alphabet):
        self.alphabet = alphabet
    
    def setKey(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ""
        for c in plaintext:
            if c in self.alphabet:
                idx = self.alphabet.index(c)
                next_idx = (idx + self.key) % len(self.alphabet)
                ciphertext += self.alphabet[next_idx]
            else:
                ciphertext += c 
                # pass -> if you want to skip this character
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        for c in ciphertext:
            if c in self.alphabet:
                idx = self.alphabet.index(c)
                prev_idx = (idx - self.key + len(self.alphabet)) % len(self.alphabet)
                plaintext += self.alphabet[prev_idx]
            else:
                plaintext += c
                # pass -> if you want to skip this character
        return plaintext