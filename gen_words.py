from random import *
from math import *

def pickrand(inlist): #choose random entry in list or list of lists
    z = random()

    if type(inlist[0]) is list:
        outlist = []
        for sublist in inlist:
            y = sublist[int(z*len(sublist))]
            outlist.append(y)
        return(outlist)
        
    else:
        y = inlist[int(z*len(inlist))]
        return(y)
            
def logbase(mu,sigma,base):
	m = log(base**mu)
	s = log(base**sigma)
	for i in range(10):
		return(lognormvariate(m,s))
##a = 0.210 #beta function fits for full English text
##b = 1.35

n = 100 # number of words desired as output

vowels = [u'i',u'ɪ',u'ʊ',u'u',u'e',u'ə',u'o',u'ɛ',u'ə',u'ʌ',u'ɔ',u'æ',u'a',u'ɑ',u'ɒ']

inventories = {} # phonemic inventories
structures = {} # [[syllable], [word]] structures
keys = {} # orthographic key
betaparams = {} # [beta function variable 'alpha', beta function variable 'beta']
sylparams = {} # p that [onset, nucleus, coda] is dropped
length = {} # [mu,sigma] for lognormal distribution
clusters = {} # acceptable clusters for [nuclei, onset, coda]; longer clusters should be listed near the end, after possible subclusters
exceptions = {} # [[forbidden onsets], [non-vowel nuclei], [forbidden codas]]

parameters = {} #to shut it up

# >>>> need syllable structure for each language
# >>>> need separate initial onset and coda probabilities
# >>>> need list of acceptable onset, coda, and nucleus clusters

##Draconic (Eastern)

inventories['Draconic'] = ['a','g',u'ɪ','i','x','d',u'ʊ',u'æ',u'dʒ','k',u'ɣ','r','e',u'θ',u'ð',u'ə','s',u'ʃ',u'tʃ']
structures['Draconic'] = [['o',[],'c'],[]]
keys['Draconic'] = [(u'ə','u'),(u'ʊ',u'ŭ'),('i','y'),(u'æ','aa'),(u'ɪ','i'),(u'θ','th'),(u'ð','th\''),('x','kh'),(u'dʒ','j'),(u'ɣ','gh'),(u'tʃ','ch'),(u'ʃr','sr'),(u'ʃ','sh')]
betaparams['Draconic'] = [0.4,1.35]
sylparams['Draconic'] = [0.1,0,0.1]
length['Draconic'] = [log(5),0.1]
clusters['Draconic'] = [[],['dr',u'θr',u'ðr',u'ʃr',u'tʃr','kr','gr','x',u'ɣr',u'kʃ'],[u'kʃ']]
exceptions['Draconic'] = [[],[],['s']]

##Dwarven (need a way to clean up double and triple consonants, also maybe indicate syllable breaks (abjad?))

inventories['Dwarven'] = ['r','l','d','n','v',u'ð','k',u'ə','b','z',u'ʒ','g','t']
structures['Dwarven'] = [['o',[],'c'],[]]
keys['Dwarven'] = [(u'ə', '\''), (u'ð', 'th'), (u'ʒ', 'j'), (u'ŋ', 'ng'), ('rrr', 'r'), ('lll', 'l'), ('rr', 'r'), ('ll', 'l'), ('nnn', 'n'), ('nn', 'n')]
betaparams['Dwarven'] = [0.7, 1.35]
sylparams['Dwarven'] = [0.25, 0.7, 0.25]
length['Dwarven'] = [log(3),0.2]
clusters['Dwarven'] = [[] , [('d', [('r',5)]), (u'ðr', [('r',5)]), ('k', [('r',5)]), ('d', [('v',5)])] , [('n', [('d',5), ('k',5), ('t',5)])]]
exceptions['Dwarven'] = [[],['r','l'],['b','v']]

##Elven

inventories['Elven'] = ['o','s',u'dʒ','e','f',u'ɪ','i','a',u'tʃ',u'ə',u'ʊ','x',u'æ',u'ʃ',u'ɑ','d','v',u'θ',u'ɣ','j',u'ð','u','p','g',u'ɲ','h','t',u'ɛ',u'ʌ',u'β',u'ɒ','r',u'ŋ','dz','n','l',u'ɔ','m','b',u'ɸ','ts','w','k','z',u'ʒ']
structures['Elven'] = ['con','vowel','(vowel)','(vowel)','(con)','(con)']
keys['Elven'] = [('e','ę'), (u'ɛ','ĕ'), (u'æ',u'ä'), ('a',u'å'), (u'ɪ',u'ı'), (u'ʊ',u'ů'), (u'ə',u'ũ'), ('u',u'ŭ'), (u'ʌ',u'ȕ'), (u'ɔ',u'ơ'), (u'ɑ',u'â'), (u'ɒ',u'ô'), ('ts','c'), ('j','y'), ('tʃ','c\''), (u'dʒ','j'), (u'ɸ','p\''), (u'β','b\''), (u'θ','th'), (u'ð','d\''), (u'ʃ','sh'), (u'ʒ','j\''), ('x','q'), (u'ɣ','g\''), (u'ŋ', 'n\''), (u'ɲ', u'ñ')]
parameters['Elven'] = [0.8, 1.35, 0.9, 19]

##Far Speech (Deep Speech)

#inventories['Far Speech'] = [

##Gnome

##Halfling

inventories['Halfling'] = ['o','i','j','n','m','a',u'ʊ','w',u'ɛ','r','l',u'ɲ',u'ŋ','l']
structures['Halfling'] = ['con','vowel','(vowel)','(con)']
keys['Halfling'] = [('i', u'ē'), (u'ɛ', u'ĕ'), (u'o', u'ŏ'), (u'ʊ', u'ō'), ('j', 'y'), (u'ŋ', 'ng'), (u'ɲ', u'ñ')]
parameters['Halfling'] = [0.5, 1.35, 0.99, 11]

##Kamadamake

inventories['Kamadamake'] = ['a','m','e','k','w','p','i','d','o','h','r','t','u',u'tʃ','f','l','n','g',u'ʃ']
structures['Kamadamake'] = [[[],'o',[]],[]]
keys['Kamadamake'] = [(u'tʃ','ch'),(u'ʃ','sh')]
betaparams['Kamadamake'] = [0.21, 1.35]
sylparams['Kamadamake'] = [0.9, 0, 0]
length['Kamadamake'] = [log(9),0.4]
clusters['Kamadamake'] = [[('i',[('a',5),('e',5),('o',5),('u',5)])],[('p', [('w', 5), ('r', 5), ('l', 5)]), ('t', [('w', 5), ('r', 5), ('l', 5)]), ('d', [('w', 5), ('r', 5), ('l', 5)]), ('k', [('w', 5), ('r', 5), ('l', 5)]), ('g', [('w', 5), ('r', 5), ('l', 5)]), ('f', [('w', 5), ('r', 5), ('l', 5)]), ('ʃ', [('w', 5), ('r', 5), ('l', 5)]), ('h', [('w', 5), ('r', 5), ('l', 5)]), ('tʃ', [('w', 5), ('r', 5), ('l', 5)]), ('m', [('w', 5), ('r', 5), ('l', 5)]), ('n', [('w', 5), ('r', 5), ('l', 5)])],[]]
exceptions['Kamadamake'] = [['w','r','l'],['ia','ie','iu','io'],['i']]
##clusters seems to open the door for multiple possible endings being attached simultaneously. how to solve?

##Mitrian

inventories['Mitrian'] = ['a','g',u'ɪ',u'ʊ',u'tʃ','r','o','s',u'ð','d','f','k','m',u'ɛ','l','b',u'ɲ','n','v','z','p',u'dʒ',u'ʒ','t',u'ʃ','h']
structures['Mitrian'] = [['o',[],'c'],[]]
keys['Mitrian'] = [(u'iɛ', 'ia'), (u'ɲ', 'ñ'), (u'dʒ', 'j'), (u'ʒ', 'jh'), (u'tʃ', 'c'), (u'ʃ', 'sh'), (u'ɪ', 'i'), (u'ʊ', 'u'), (u'ɛ', 'e')]
betaparams['Mitrian'] = [0.21, 1.35]
sylparams['Mitrian'] = [0.1, 0, 0.2]
length['Mitrian'] = [log(6), 0.25]
clusters['Mitrian'] = [[(u'i',[('ɛ',5)])],[(u'tʃ',[('r',5)]),(u'ð',[('r',5)]),('d',[('r',5)]),('t',[('r',5)])],[]]
exceptions['Mitrian'] = [[],[],[u'ɲ']]

##Orcish (Scarian)

inventories['Orcish'] = [u'æ','z',u'ɔ','g','r',u'ɑ','d','a','n',u'ə',u'ɣ',u'ʌ','o',u'dʒ',u'ð',u'ʒ','w',u'ɔə','v']
structures['Orcish'] = [['o',[],'c'],[]]
keys['Orcish'] = [(u'ɣ', 'gh'), (u'ð', 'th'), ('j', 'y'), (u'dʒ', 'j'), (u'ʒ', 'j\''), ('a', 'a\''), ('o', 'o\''), (u'ɔə', 'o'), (u'ʌ', 'u\''), (u'ə', 'u'), (u'ɔ', u'ā'), (u'ɑ', 'a\''), (u'æ', 'a')]
betaparams['Orcish'] = [0.75, 1.35]
sylparams['Orcish'] = [0.1, 0, 0.05]
length['Orcish'] = [log(5), 0.15]
clusters['Orcish'] = [[],[],[]]
exceptions['Orcish'] = [[],[],[]]

##Sark

inventories['Sark'] = [u'ɪə',u'ʒ',u'ə','n','a',u'eɪ','d',u'ɛ',u'aɪ',u'θ','u',u'ʃ','r',u'ʊ','m','k',u'ɪ','l','g',u'dʒ','j','s','t']
##inventories['Sark'] = [u'ɪə',u'eɪ','t',u'ə','j',u'ɪ','a','m','d','h','v','k','r','f',u'ɛ',u'aɪ',u'ʊ',u'dʒ','u','l',u'θ',u'ʃ','g','s','n',u'ʒ']
structures['Sark'] = [['o',[],'c'],[]]
keys['Sark'] = [(u'eɪ','ay'), (u'ʊ', 'uy'), ('u', 'o'), ('j', 'y'), (u'dʒ', 'j'), (u'ʒ', 'zh'), (u'ʃ', 'sh'), (u'θ', 'th'), (u'ɪə', 'i'), (u'aɪ', 'iy'), (u'ɪ', 'y'), (u'ə', 'u'), (u'ɛ', 'e')]
betaparams['Sark'] = [0.3, 1.35]
sylparams['Sark'] = [0.01, 0, 0.4]
length['Sark'] = [log(6), 0.2]
clusters['Sark'] = [[('a',[('r',5),('l',5)]),(u'ɪə',[('r',5),('l',5)]),(u'ə',[('r',5),('l',5)])],[('d',[('r',5)]),('f',[('r',5)]),('g',[('r',5)])],[]]
##clusters['Sark'] = [['ar','al','ir','il','ur','ul'],['hv','dr','fr','gr'],[]]
exceptions['Sark'] = [[],[],['j','s']]##,u'ʒ',u'ʃ','g','d',u'θ']] if these later four are added to non-terminal syllable, ignore them. If syllable is terminal, end syllable before the phone and append syllable consisting of phone + schwa (or carrot?)

##declare language

lang = 'Sark'

phonemes = inventories[lang]
rules = structures[lang][0]
key = keys[lang]
alpha = betaparams[lang][0]
beta = betaparams[lang][1]
sylpars = sylparams[lang]
mu = length[lang][0]
sigma = length[lang][1]
clust = clusters[lang]
excepts = exceptions[lang]

if len(clust) == 2: ## if onset and coda share acceptable clusters
    clust.append(clust[1])


##con = [] #list of consonants
##vwl = [] #list of vowels

# list of approximants?
# tones?

sounds = []
glyphs = []
guide = [0]*len(phonemes) #######

##total = 0
##jj = 0

while len(sounds) < 10*n: ##(vwl) < 5*n or len(con) < 10*n:
    x = int(betavariate(alpha,beta)*len(phonemes))
    guide[x] += 1 ########
    x = phonemes[x]
    sounds.append(x)
    z = 0
    for item in key:
        if x == item[0]:
            glyphs.append(item[1])
            z = 1
    if z == 0:
        glyphs.append(x)
##    if x[0] in vowels:
##        vwl.append(x)
##    else:
##        con.append(x)

onsets = [] #list of onsets
nuclei = [] #list of nuclei
codas = [] #list of codas
g_onsets = [] #list of onset glyphs
g_nuclei = [] #list of nucleus glyphs
g_codas = [] #list of coda glyphs

i = 0

##cl = []
    
while len(onsets) <= 2*n or len(nuclei) <= 2*n or len(codas) <= 2*n:
    a = sounds[i]
    b = glyphs[i]
    x = 0

    if a[0] in vowels + excepts[1]: ##What if consonants can be both syllabic and regular?
        for item in clust[0]: ##creating clusters
            if item[0] == a:
                for entry in item[1]:
                    clip = sounds[i+1:i+1+entry[1]]
                    if entry[0] in clip:
                        i += 1
                        c = clip.index(entry[0])
                        s = sounds[i+c]
                        g = glyphs[i+c]
                        a += s
                        b += g                       
                        del sounds[i+c]
                        del glyphs[i+c]
                        sounds.insert(i,s)
                        glyphs.insert(i,g)
##                        cl.append((a,b))
##        while a + sounds[i + 1] in clust[0]:
##            a += sounds[i + 1]
##            b += glyphs[i + 1]
##            i += 1
        nuclei.append(a)
        g_nuclei.append(b)
    elif a in excepts[0]:
        x = 2
    elif a in excepts[2]:
        x = 1
    else:
        x = randint(1,2)
##    if x >= 1: ## figuring out adjustment rate for u'ʒ' in Sark
##        total += 1
##        if a == u'ʒ':
##            jj += 1

    if x == 1:
        for item in clust[1]: ##creating clusters
            if item[0] == a:
                for entry in item[1]:
                    clip = sounds[i+1:i+1+entry[1]]
                    if entry[0] in clip:
                        i += 1
                        c = clip.index(entry[0])
                        s = sounds[i+c]
                        g = glyphs[i+c]
                        a += s
                        b += g                       
                        del sounds[i+c]
                        del glyphs[i+c]
                        sounds.insert(i,s)
                        glyphs.insert(i,g)
##                        cl.append((a,b))
##        while a + sounds[i + 1] in clust[1]:
##            a += sounds[i + 1]
##            b += glyphs[i + 1]
##            i += 1
        onsets.append(a)
        g_onsets.append(b)
    elif x == 2:
        for item in clust[2]: ##creating clusters
            if len(item) > 0:
                if item[0] == a:
                    for entry in item[1]:
                        clip = sounds[i+1:i+1+entry[1]]
                        if entry[0] in clip:
                            i += 1
                            c = clip.index(entry[0])
                            s = sounds[i+c]
                            g = glyphs[i+c]
                            a += s
                            b += g                       
                            del sounds[i+c]
                            del glyphs[i+c]
                            sounds.insert(i,s)
                            glyphs.insert(i,g)
##                        cl.append((a,b))
##        while a + sounds[i + 1] in clust[2]:
##            a += sounds[i + 1]
##            b += glyphs[i + 1]
##            i += 1
        codas.append(a)
        g_codas.append(b)

    i += 1
    if i >= (10*n) - 10:
        i = randint(0,int(n/2))

if 'o' not in rules:
    codas += onsets
    g_codas += g_onsets
elif 'c' not in rules:
    onsets += codas
    g_onsets += g_codas

syls = []# list of syllables
g_syls = []

for i in range(2*n):
    a = ''
    b = ''
    for j in range(len(rules)):
        if random() > sylpars[j]:
            #z = random()
            if rules[j] == 'o':
                m = pickrand([onsets,g_onsets])
                a += m[0]
                b += m[1]
                #a += onsets[int(z*len(onsets))]
                #b += g_onsets[int(z*len(g_onsets))] ##could make function for this
            elif rules[j] == 'c':
                m = pickrand([codas,g_codas])
                a += m[0]
                b += m[1]
                #a += codas[int(z*len(codas))]
                #b += g_codas[int(z*len(g_codas))]
            else:
                m = pickrand([nuclei,g_nuclei])
                a += m[0]
                b += m[1]
                #a += nuclei[int(z*len(nuclei))]
                #b += g_nuclei[int(z*len(g_nuclei))]
    syls.append(a)
    g_syls.append(b)



words = []
orths = []

for i in range(n):
    a = ''
    b = ''
    j = round(lognormvariate(mu,sigma))
    while len(a) < j:
        m = pickrand([syls,g_syls])
        a += m[0] + '.'
        b += m[1]
##        z = random()
##        a += syls[int(z*len(syls))]
##        b += g_syls[int(z*len(g_syls))]
    words.append(a[0:-1])
    orths.append(b)
    print(a + ' | ' + b.capitalize())

gcount = float(sum(guide))
d = 0
i = 0
for item in guide:
    item = item/gcount*100
    item += d
    d = item
    guide[i] = item
    i += 1
print(guide)
print(phonemes)

##print(cl)
    
# orthography and clean-up can be copied over?
# other adjustments?


# >>>> need word structure(s) for each language??????
# list of words

##print(total)
##print(jj)
##print(jj/total)
