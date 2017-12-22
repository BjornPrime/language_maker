# -*- coding: utf-8 -*-
from random import *

a = 0.210 #beta function fits for full English text
b = 1.35

vowels = [u'i',u'ɪ',u'ʊ',u'u',u'e',u'ə',u'o',u'ɛ',u'ə',u'ʌ',u'ɔ',u'æ',u'a',u'ɑ',u'ɒ']

inventories = {} #phonemic inventories
structures = {} #syllable structures
keys = {} #orthographic key
parameters = {} #several constants affecting letter frequency and word length -- [beta function variable 'a', beta function variable 'b', probability that option phoneme will be dropped, (max word length in syllables)**2]

##Draconic

##Dwarven

inventories['Dwarven'] = ['r','l','d','n','v',u'ð','k',u'ə','b','z',u'ʒ','g','t']
structures['Dwarven'] = [[u'ə'],'con','(con)',['r','l','n'],'(con)']
keys['Dwarven'] = [(u'ə', '\''), (u'ð', 'th'), (u'ʒ', 'j'), (u'ŋ', 'ng'), ('rrr', 'r'), ('lll', 'l'), ('rr', 'r'), ('ll', 'l'), ('nnn', 'n'), ('nn', 'n')]
parameters['Dwarven'] = [0.7, 1.35, 0.25, 1.7]

##Elven

inventories['Elven'] = ['o','s',u'dʒ','e','f',u'ɪ','i','a',u'tʃ',u'ə',u'ʊ','x',u'æ',u'ʃ',u'ɑ','d','v',u'θ',u'ɣ','j',u'ð','u','p','g',u'ɲ','h','t',u'ɛ',u'ʌ',u'β',u'ɒ','r',u'ŋ','dz','n','l',u'ɔ','m','b',u'ɸ','ts','w','k','z',u'ʒ']
structures['Elven'] = ['con','vowel','(vowel)','(vowel)','(con)','(con)']
keys['Elven'] = [('e','ę'), (u'ɛ','ĕ'), (u'æ',u'ä'), ('a',u'å'), (u'ɪ',u'ı'), (u'ʊ',u'ů'), (u'ə',u'ũ'), ('u',u'ŭ'), (u'ʌ',u'ȕ'), (u'ɔ',u'ơ'), (u'ɑ',u'â'), (u'ɒ',u'ô'), ('ts','c'), ('j','y'), ('tʃ','c\''), (u'dʒ','j'), (u'ɸ','p\''), (u'β','b\''), (u'θ','th'), (u'ð','d\''), (u'ʃ','sh'), (u'ʒ','j\''), ('x','q'), (u'ɣ','g\''), (u'ŋ', 'n\''), (u'ɲ', u'ñ')]
parameters['Elven'] = [0.8, 1.35, 0.9, 19]

##Halfling

inventories['Halfling'] = ['o','i','j','n','m','a',u'ʊ','w',u'ɛ','r','l',u'ɲ',u'ŋ','l']
structures['Halfling'] = ['con','vowel','(vowel)','(con)']
keys['Halfling'] = [('i', u'ē'), (u'ɛ', u'ĕ'), (u'o', u'ŏ'), (u'ʊ', u'ō'), ('j', 'y'), (u'ŋ', 'ng'), (u'ɲ', u'ñ')]
parameters['Halfling'] = [0.5, 1.35, 0.99, 11]

##Mitrian

inventories['Mitrian'] = ['a','g',u'ɪ',u'ʊ',u'tʃ','r','o','s',u'ð','d','f','k',u'iə','m',u'ɛ','l','b',u'ɲ','n','v','z','p',u'dʒ',u'ʒ','t',u'ʃ','h']
structures['Mitrian'] = ['(con)',['r','*'],'vowel','(con)']
keys['Mitrian'] = [(u'ɲ', 'ñ'), (u'dʒ', 'j'), (u'ʒ', 'jh'), (u'tʃ', 'c'), (u'ʃ', 'sh'), (u'ɪ', 'i'), (u'ʊ', 'u'), (u'ɛ', 'e'), (u'iə', 'ia')]
parameters['Mitrian'] = [0.21, 1.35, 0.1, 8]

##Orcish

inventories['Orcish'] = [u'æ','z',u'ɔ','g','r',u'ɑ','d','a','n',u'ə',u'ɣ',u'ʌ','o',u'dʒ',u'ð',u'ʒ','w','h',u'ɔə','v']
structures['Orcish'] = ['(con)','vowel','(con)']
keys['Orcish'] = [(u'ɣ', 'gh'), (u'ð', 'th'), ('j', 'y'), (u'ʒ', 'j'), ('a', 'a\''), ('o', 'o\''), (u'ɔə', 'o'), (u'ʌ', 'u\''), (u'ə', 'u'), (u'ɔ', u'ā'), (u'ɑ', 'a\''), (u'æ', 'a')]
parameters['Orcish'] = [0.75, 1.35, 0.1, 5]

##Sark (unfinished)

inventories['Sark'] = [u'ɪə','t',u'ə','j',u'ɪ','a','m','d','h','v','k','r','f',u'ɛ',u'aɪ',u'dʒ','u','l',u'θ',u'ʃ','g','s','n',u'ʒ']
structures['Sark'] = ['(con)','vowel',['r','l'],'(con)']
keys['Sark'] = [('u', 'o'), ('j', 'y'), (u'dʒ', 'j'), (u'ʒ', 'zh'), (u'ʃ', 'sh'), (u'θ', 'th'), (u'ɪə', 'i'), (u'aɪ', 'iy'), (u'ɪ', 'y'), (u'ə', 'u'), (u'ɛ', 'e')]
parameters['Sark'] = [0.5, 1.35, 0.01, 4.2] 

##declare language

lang = 'Sark'

phonemes = inventories[lang]
rules = structures[lang]
pars = parameters[lang]
key = keys[lang]

a = pars[0] #beta function parameter
b = pars[1] #beta function parameter
c = pars[2] #probability that optional slots aren't filled
d = pars[3] #determines average word length

##generate syllables

syllables = []

####i = 0
####s = set()
####
####while i < 200:
####    grab = []
####    syl = ''
####    for j in range(len(rules)):
####        new = phonemes[int(betavariate(a,b)*len(phonemes))]
####        grab.append(new)
####    k = 0
####    l = 0
####    while l < len(rules):
####        if ('con' in rules[l] and grab[k][0] not in vowels) or ('vowel' in rules[l] and grab[k][0] in vowels):
####            syl += grab[k]
####        elif '(' not in rules[l]:
####            l -= 1
####        else:
####            k -= 1
####
####        k += 1
####        l += 1
####        
####        if k >= len(grab):
####            l = len(rules)
####            syl = ''
####
####    if syl != '':
####        syllables.append(syl)
####        s.add(syl)
####        if len(s) == i:
####            del syllables[-1]
####        i = len(s)
####
####for i in range(100):
####    print(syllables[i])
            
####the below and above both work, but I think below is better:
                                  
for i in range(1000):
    syl = ''
    pre = 0
    for item in rules:
        phone = phonemes[int(betavariate(a,b)*len(phonemes))]
        if '(' in item:
            r = random()
            if r < c:
                phone = ''
        elif type(item) is list:
            if item[-1] == '*' and ( phone not in item or pre == 0 ):
                phone = ''
            elif phone not in item:
                phone = ''
                
        pre = 0
        if phone != '':
            pre = 1  
            if 'con' in item:
                while phone[0] in vowels:
                    phone = phonemes[int(betavariate(a,b)*len(phonemes))]
            if 'vowel' in item:
                while phone[0] not in vowels:
                    phone = phonemes[int(betavariate(a,b)*len(phonemes))]

        syl += phone
                                  
    syllables.append(syl)

#combine syllables into words

phones = []

for i in range(100):
    word = syllables[int(random()*len(syllables))]
    i = 1
    r = random()*d
    while i**2 < r:
        word += syllables[int(random()*len(syllables))]
        i += 1
        
    phones.append(word)
    

##assimilation

##transcription from phonemes to orthography

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
