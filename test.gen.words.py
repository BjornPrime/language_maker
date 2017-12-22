# -*- coding: utf-8 -*-
from random import *


vowels = [u'i',u'ɪ',u'ʊ',u'u',u'e',u'ə',u'o',u'ɛ',u'ə',u'ʌ',u'ɔ',u'æ',u'a']		ɑ/ɒ

Inventories = {}
Inventories['Orcish'] = ['z','',u'æ',u'ɑ',u'ͻ','g','r','n','h','a',u'ʒ',

#Scarian Orcish
consonant = [('z', 4), ('g', 2), (u'gʰ', 1), ('d', 1), ('r', 2), ('', 4), (u'dʒ', 1), ('v', 0.5), (u'ð', 1), (u'ʒ', 1.5), ('w', 0.75), ('n', 2), ('h', 2)]
vowel = [('a', 2), (u'ʌ', 1), ('o', 1), (u'ͻ', 3), (u'ə', 1.5), (u'ɑ', 4), (u'æ', 4), (u'ɔə', 0.75)]
#final = [('z', 1), ('sh', 1), ('', 1)]

freqs = [consonant,vowel,consonant]#,onset2,vowel2,final2]
k = 0
for freq in freqs:
    new = []
    z = 0
    l = 0
    for item in freq:
        z += item[1]
        freq[l] = (item[0], z)
        l += 1
    freqs[k] = freq
    k += 1

syllables = []

for i in range(100):
    syl = ''
    for freq in freqs:
        r = freq[-1][1]*random()
        m = 0
        while freq[m][1] < r:
            m += 1
        syl += freq[m][0]
    syllables.append(syl)

phones = []

for i in range(100):
    r = randint(1,10)
    word = ''
    s = 1
    while s**2 <= r:
        word += choice(syllables)
        s += 1
    phones.append(word)

##assimilation

##transcription from phonemes to orthography

key = [(u'ʰ', 'h'), (u'ð', 'th'), ('j', 'y'), (u'ʒ', 'j'), ('a', 'a\''), ('o', 'o\''), (u'ɔə', 'o'), (u'ʌ', 'u\''), (u'ə', 'u'), (u'ͻ', '\'a'), (u'ɑ', 'a\''), (u'æ', 'a')]
orths = []
for word in phones:
    item = word
    writ = word
    for rule in key:
        if rule[0] in item:
            writ = writ.replace(rule[0],rule[1])
            item = item.replace(rule[0], 'X')
    orths.append(writ.capitalize())

i = 0
for word in phones:
    print(word + ' | ' + orths[i])
    i += 1
##final clean up


##    print(freq)
##    x = 1
##    for item in freq:
##        s = str(item[1])
##        if '.' in s: #extract common denominator from float
##            y = s.index('.')
##            x *= 1/float(s[y:])
####            j = 0
####            for item in freq: #multiply cnt by denominator
####                if i == j:
####                    new = (item[0], int(item[1]*x))
####                    freq[j] = new
####                else:
##    i = 0                  
##    for item in freq:
##        new = (item[0], round(item[1]*x))
##        freq[i] = new        
##        i += 1
##    print(freq)
####    print(x)

'''
INSTRUCTIONS
-Define your phonemes for each syllable inside the square brackets below.
-Each phoneme has a weight assigned to it inside the round bracket, e.g ('s', 5). Change this number to change the probability of it being selected.
-For instance, ('s', 5) means that 's' is 5 times more likely to appear than 't', which is ('t', 1).
-Fractions can be used to lower the probability -- ('p', 1/3).
'''

#This part of the code handles the weighting of the phonemes and feeds into the code below.
##onset_weight = [val for val, cnt in onset for i in range(cnt)]
##vowel_weight = [val for val, cnt in vowel for i in range(cnt)]
##final_weight = [val for val, cnt in final for i in range(cnt)]
##onset_weight2 = [val for val, cnt in onset2 for i in range(cnt)]
##vowel_weight2 = [val for val, cnt in vowel2 for i in range(cnt)]
##final_weight2 = [val for val, cnt in final2 for i in range(cnt)]
##
##
###This part of the code defines what the syllables are made of, and then defines what the word is made of.
###Syllables 2 and 3 have the added feature of a "no_syllable", without which all words would be 3 syllables long.
###Probablity of no_syllable can be increased by timesing it (*) by a number.
##
##for i in range(100): # <--- This loops everything indented below it. Change the number in range() to change the number of words generated.
##    syllable1 = random.choice(onset_weight) + random.choice(vowel_weight) + random.choice(final_weight)
##    syllable2 = random.choice(((no_syllable) * 1) + [random.choice(onset_weight2) + random.choice(vowel_weight2) + random.choice(final_weight2)])
##    syllable3 = random.choice(((no_syllable) * 3) + [random.choice(onset_weight2) + random.choice(vowel_weight2) + random.choice(final_weight2)])
##    word = syllable1 + syllable2 + syllable3
##    print(word)
