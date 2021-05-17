class Rail_fence:
    def __init__(self, key):
        assert type(key) == int, "key must be at integer"
        self.setKey(key)    
    
    def setKey(self, key):
        self.key = key

    def encrypt(self, plaintext):
        fence = [[] for i in range(self.key)]

        rail = 0
        step = 1
        
        for char in plaintext:
            fence[rail].append(char)
            rail += step

            if rail == self.key - 1 or rail == 0:
                step *= -1
        
        ciphertext = ''
        for row in fence:
            for char in row:
                ciphertext += char
        return ciphertext        
    
    def decrypt(self, ciphertext):
        fence = [[] for i in range(self.key)]

        rail = 0
        step = 1
        
        for char in ciphertext:
            fence[rail].append(char)
            rail += step

            if rail == self.key - 1 or rail == 0:
                step *= -1
        
        reverseFence = [[] for i in range(self.key)]

        ridx = 0
        idx = 0

        for row in fence:
            for _ in range(len(row)):
                reverseFence[ridx].append(ciphertext[idx])
                idx += 1
            ridx += 1
        
        rail = 0
        step = 1

        plaintext = ''
        for row in range(len(ciphertext)):
            plaintext += reverseFence[rail][0]
            reverseFence[rail].remove(reverseFence[rail][0])

            rail += step
            if rail == self.key - 1 or rail == 0:
                step *= -1

        return plaintext        
