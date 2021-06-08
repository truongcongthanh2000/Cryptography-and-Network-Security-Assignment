# run code: python gen.py > input.txt
# with small ciphertext: ciphertext = random.choice(list_ciphertext_small)
# with large ciphertext: ciphertext = random.choice(list_ciphertext)

# input format:
# ciphertext 
# keyCaesar 
# keyRail-fence

import random
import numpy as np

LIMITS = 50
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
list_ciphertext = [
    # 'ICANGETBYTHEESCAPEDCONVICTFALLINGINTOANOPENAIRPARTICLEACCELERATOR(WEHAVEONEINTHEVACANTLOTNEXTDOORANDIAMALWAYSTELLINGMY8YEAROLDTOSTOPPLAYINGNEARIT),ICANEVENGETBYTHESPACESLIMELANDINGCOINCIDENTLYMETRESFROMPETERANDJUMPINGONHISBIKE...WHATICANTGETPASTISMARYJANE.WHATAFUCKINGBITCH.INTHEFIRSTMOVIESHEISLETTINGTHESCHOOLBULLYDOHER,THENSHELETSTHERICHGUY,THENPETERHASATURN.INTHESECONDMOVIESHEGOESTHROUGHABOUTEIGHTEENDIFFERENTGUYSBEFOREABANDONINGHERBIGEXPENSIVEWEDDINGAFTERREALISINGPETERISSPIDERMAN.INTHETHIRDFILMITHINKSHEDOESABOUTSIXTYGUYSANDWHINGESALOTABOUTPETERSAVINGLIVESINSTEADOFCOMINGTOTHETHEATRETOWATCHHERCRAPACTING.WHYDOESHEPUTUPWITHHER?ITMAKESNOSENSEANDISTHEONEGLARINGDISCREPANCYINANOTHERWISECOMPLETELYSCIENTIFICALLYBELIEVABLEMOVIE',
    'I can get by the escaped convict falling into an open air particle accelerator (we have one in the vacant lot next door and I am always telling my 8 year old to stop playing near it), I can even get by the space slime landing coincidently metres from Peter and jumping on his bike... What I cant get past is Mary Jane. What a fucking bitch. In the first movie she is letting the school bully do her, then she lets the rich guy, then Peter has a turn. In the second movie she goes through about eighteen different guys before abandoning her big expensive wedding after realising Peter is spiderman. In the third film I think she does about sixty guys and whinges a lot about peter saving lives instead of coming to the theatre to watch her crap acting. Why does he put up with her? It makes no sense and is the one glaring discrepancy in an otherwise completely scientifically believable movie',
    'Did you see the President speak about gun control today? It’s important. Probably the most important problem of our time and we have to solve it. Here’s what he said today: THE PRESIDENT: Happy New Year, everybody. Before the New Year, I mentioned that I had given the charge to my Attorney General, FBI Director, Deputy Director at the ATF, and personnel at my White House to work together to see what more we could do to prevent a scourge of gun violence in this country. I think everybody here is all too familiar with the statistics. We have tens of thousands of people every single year who are killed by guns. We have suicides that are committed by firearms at a rate that far exceeds other countries. We have a frequency of mass shootings that far exceeds other countries in frequency. And although it is my strong belief that for us to get our complete arm around the problem Congress needs to act, what I asked my team to do is to see what more we could do to strengthen our enforcement and prevent guns from falling into the wrong hands to make sure that criminals, people who are mentally unstable, those who could pose a danger to themselves or others are less likely to get them. And I’ve just received back a report from Attorney General Lynch, Director Comey, as well as Deputy Director Brandon about some of the ideas and initiatives that they think can make a difference. And the good news is, is that these are not only recommendations that are well within my legal authority and the executive branch, but they’re also ones that the overwhelming majority of the American people, including gun owners, support and believe. So over the next several days, we’ll be rolling out these initiatives. We’ll be making sure that people have a very clear understanding of what can make a difference and what we can do. And although we have to be very clear that this is not going to solve every violent crime in this country, it’s not going to prevent every mass shooting, it’s not going to keep every gun out of the hands of a criminal, it will potentially save lives and spare families the pain and the extraordinary loss that they’ve suffered as a consequence of a firearm getting in the hands of the wrong people. I’m also confident that the recommendations that are being made by my team here are ones that are entirely consistent with the Second Amendment and people’s lawful right to bear arms. And we’ve been very careful recognizing that, although we have a strong tradition of gun ownership in this country, that even though it’s who possess firearms for hunting, for self-protection, and for other legitimate reasons, I want to make sure that the wrong people don’t have them for the wrong reasons. So I want to say how much I appreciate the outstanding work that the team has done. Many of you worked over the holidays to get this set of recommendations to me. And I’m looking forward to speaking to the American people over the next several days in more detail about it. Thank you very much, everybody. Regardless of where you stand on the matter, we have to change some things. Back to tech. Are you at CES? I’m not this year. Mostly because there’s a lot of germs and I shouldn’t be around them if I can help it. I’m pretty sure my dogs would have liked it though, because there’s a lot of tech in Vegas for all kinds of people (and pets). If you were a dog would you want a phone? Or a self-feeding thing? Of course you would. You’d have to sit around all day watching your parents use technology while you sit around and lick yourself. What kind of existence is that? I know, right? I hope there’s some dog tech that comes out of the conference, otherwise it’s a wash.',
    'I think what JFK meant was just because things aren’t going your way doesn’t mean that it won’t eventually. You have to play the long game, you have to stick in there and see things as far as you can possibly see them. It’s like Twitter. People are worried about whether Twitter can weather the storm of lack of growth. I think it can. What about the character count? Well, I personally feel like asking people to keep their thoughts shorter make them more powerful. They’re easier to share. Repeat, etc. What will happen when people can put this much text in a tweet? I don’t know. I do know that I don’t want to spend hours reading tweets because I like the fact that I can glance at the app and figure out what’s going on pretty quickly.',
    'Let’s say an aspiring writer is working on a story. Their goal is 10,000 words. For this example, the writer uses Google Docs. If the writer follows the typical manuscript format – 12pt Calibri font with double spacing – they will have a short story that is approximately 34 pages. If that writer writes a 50,000-word novel, the total manuscript page count will be about 172 pages. However, that does not take into account the story being broken down into chapters or the use of line breaks. Therefore, the page count for one 50,000-word novel will very likely differ from the page count of another novel with the same word count since the book\'s layout will have to be taken into account.'
]

list_ciphertext_small = [
    'I am a student at Ho Chi Minh University of Technology'
]
# list_ciphertext.append(some ciphertext)
# ciphertext = random.choice(list_ciphertext)

ciphertext = random.choice(list_ciphertext_small)

print(ciphertext)
keyCaesar = random.randint(0, len(alphabet) - 1)
print(keyCaesar)

keyRail_fence = random.randint(2, min(LIMITS, len(ciphertext) - 1))
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