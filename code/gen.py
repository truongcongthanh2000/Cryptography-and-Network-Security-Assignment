# run code: python gen.py > input.txt
# with small ciphertext: ciphertext = random.choice(list_ciphertext_small)
# with large ciphertext: ciphertext = random.choice(list_ciphertext)

# input format:
# ciphertext 
# keyCaesar 
# keyRail-fence

import random
import numpy as np

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
list_ciphertext = [
    'ICANGETBYTHEESCAPEDCONVICTFALLINGINTOANOPENAIRPARTICLEACCELERATOR(WEHAVEONEINTHEVACANTLOTNEXTDOORANDIAMALWAYSTELLINGMY8YEAROLDTOSTOPPLAYINGNEARIT),ICANEVENGETBYTHESPACESLIMELANDINGCOINCIDENTLYMETRESFROMPETERANDJUMPINGONHISBIKE...WHATICANTGETPASTISMARYJANE.WHATAFUCKINGBITCH.INTHEFIRSTMOVIESHEISLETTINGTHESCHOOLBULLYDOHER,THENSHELETSTHERICHGUY,THENPETERHASATURN.INTHESECONDMOVIESHEGOESTHROUGHABOUTEIGHTEENDIFFERENTGUYSBEFOREABANDONINGHERBIGEXPENSIVEWEDDINGAFTERREALISINGPETERISSPIDERMAN.INTHETHIRDFILMITHINKSHEDOESABOUTSIXTYGUYSANDWHINGESALOTABOUTPETERSAVINGLIVESINSTEADOFCOMINGTOTHETHEATRETOWATCHHERCRAPACTING.WHYDOESHEPUTUPWITHHER?ITMAKESNOSENSEANDISTHEONEGLARINGDISCREPANCYINANOTHERWISECOMPLETELYSCIENTIFICALLYBELIEVABLEMOVIE',
    'I can get by the escaped convict falling into an open air particle accelerator (we have one in the vacant lot next door and I am always telling my 8 year old to stop playing near it), I can even get by the space slime landing coincidently metres from Peter and jumping on his bike... What I cant get past is Mary Jane. What a fucking bitch. In the first movie she is letting the school bully do her, then she lets the rich guy, then Peter has a turn. In the second movie she goes through about eighteen different guys before abandoning her big expensive wedding after realising Peter is spiderman. In the third film I think she does about sixty guys and whinges a lot about peter saving lives instead of coming to the theatre to watch her crap acting. Why does he put up with her? It makes no sense and is the one glaring discrepancy in an otherwise completely scientifically believable movie'
]

list_ciphertext_small = [
    'Cryptography',
    'and',
    'Network',
    'Security',
    'HCMUT'
]
# list_ciphertext.append(some ciphertext)
# ciphertext = random.choice(list_ciphertext)

ciphertext = random.choice(list_ciphertext_small)

print(ciphertext)
keyCaesar = random.randint(0, len(alphabet) - 1)
print(keyCaesar)

keyRail_fence = random.randint(2, min(50, len(ciphertext) - 1))
print(keyRail_fence)

# alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# def printRAW(*Text):
#     RAWOut = open(1, 'w', encoding='utf8', closefd=False)
#     print(*Text, file=RAWOut)
#     RAWOut.flush()
#     RAWOut.close()

# TestText = "Test - āĀēĒčČ..šŠūŪžŽ" # this not UTF-8...it is a Unicode string in Python 3.X.
# TestText2 = TestText.encode('utf8') # this is a UTF-8-encoded byte string.

# import sys
# sys.stdout.buffer.write(TestText2)

# from random import choice
# import string 
# alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# b = string.printable
# print(b)
# print(alphabet)
# print(len(b))
# print(len(alphabet))

# alphabet = ""
# numeral = []
# for n in range(65536):
#     alphabet += chr(n)
#     numeral.append(n)

# printRAW(alphabet.decode('cp1252').encode('utf-8'))
# # print(numeral)
# # assert alphabet == b, "false"