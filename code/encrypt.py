from caesarCipher import Caesar
from rail_fenceCipher import Rail_fence

class Encrypt:
    def __init__(self, alphabet, keyCaesar, keyRail_fence):
        self.caesarCipher = Caesar(alphabet, keyCaesar)
        self.rail_fenceCipher = Rail_fence(keyRail_fence)

    def encrypt(self, plaintext):
        answer = []
        # Caesar Cipher
        # print('Encode with Caesar Cipher:')
        ciphertext = self.caesarCipher.encrypt(plaintext)
        answer.append(ciphertext)
        # print('ciphertext = ', ciphertext)

        # Rail Fence Cipher
        # print('Encode with Rail Fence Cipher:')
        ciphertext = self.rail_fenceCipher.encrypt(plaintext)
        answer.append(ciphertext)
        # print('ciphertext = ', ciphertext)

        # Rail_fence(Caesar(plaintext))
        # print('Encode with product encryption Rail_fence x Caesar')
        ciphertext = self.rail_fenceCipher.encrypt(self.caesarCipher.encrypt(plaintext))
        answer.append(ciphertext)
        
        return answer
