from math import *
from random import *

class Language:
    parts = ['onset','medial','nucleus','coda']

    def __init__(self, onset, medial, nucleus, coda, orthography, wordlength, clusters = {}, structure = [1,0,1,1], alpha = 0.4, beta = 1.35):#'structure' lists probabilty of occurence of [onset,medial,nucleus,coda]; 'parameters' lists constants for phomene distribution (either exponential or beta)

        self.structure = structure

        self.phonemes = {}
        self.phonemes['onset'] = onset
        self.phonemes['medial'] = medial
        self.phonemes['nucleus'] = nucleus
        self.phonemes['coda'] = coda

        self.allsounds = set(onset + medial + nucleus + coda)##Set of all phonemes in language

        self.orths = orthography ##Do we need support for orthography varying by phoneme position

        self.allsyls = [] ## list of all syllables created 
        self.sylcount = 0 ## # of syllables created
        self.sylfreqs = {} ## keys are syllables, entries are how many times they've appeared
        self.syllables = []

        self.wordlist = [] #words are saved as 'sounds|glyph' format strings, not as gen_language.Word objects
        self.wordcount = 0
        self.wordfreqs = {}

        self.length = wordlength

        self.clusters = clusters

        self.alpha = alpha
        self.beta = beta

    def choose(self,position):#picking a phoneme from the list for its position

        phonelist = self.phonemes[position]
        x = int(betavariate(self.alpha,self.beta)*len(phonelist))
        y = phonelist[x]

        if len(self.clusters) > 0:
            if y in self.clusters.keys() and position != 'coda': #this can only do 2-clusters and can't handle coda clusters well

                base = y
                options = self.clusters[base]

                if random() < options[0]:
                    y = choice(options[1:])             
        
        return(y)

    def glyph(self,phoneme):#takes a phoneme and returns the associated glyph

        if phoneme in self.orths.keys():
            x = self.orths[phoneme]
        else:
            x = phoneme

        return(x)

    def glyphify(self,syllable): #turns a syllable, as defined by dictionary of position:phoneme entrys, into writing 

        partlist = []
        output = ''
        
        for item in self.parts: #determining which syllable components this syllable contains
            if item in syllable.keys():
                partlist.append(item)

        for item in partlist: #determining the glyph from the phoneme at each position 
            x = syllable[item]
            if x in self.allsounds:
                y = self.glyph(x)
            elif x[0:-1] and x[-1] in self.allsounds:
                a = self.glyph(x[0:-1])
                b = self.glyph(x[-1])
                y = a + b
            elif x[0] and x[1:3] in self.allsounds:               
                a = self.glyph(x[0])
                b = self.glyph(x[1:3])
                y = a + b
            else:
                a = self.glyph(x[0])
                b = self.glyph(x[1])
                c = self.glyph(x[2])
                y = a + b + c
                
            output += y

        return(output)

    def pickwords(self, n = 1):

        for i in range(n):

            print(choice(self.wordlist))

        return(None)

    def salient(self, n = 10000):

        self.syllables = []
        y = 0.5
        
        while len(self.allsyls) < n:
            z = Syllable(self)

        for item in self.allsyls:
            
            for i in range(ceil(self.sylfreqs[item]**y)):
                
                syllables.append(item)
                

class Syllable:#
    def __init__(self, language):
        self.positions = {}
        self.filled = []

        for item in language.parts: #creating random syllable
            
            x = language.parts.index(item)
            frequency = language.structure[x]
            phonelist = language.phonemes[item]

            if frequency >= random() and len(phonelist) > 0:
                
                self.filled.append(item)
                self.positions[item] = language.choose(item)
                

        self.sounds = ''
        self.written = language.glyphify(self.positions)
               
        for item in self.filled: #creating syllable's string representation as both written and spoken
            s = self.positions[item]
            self.sounds += s

        self.syl = self.sounds + '|' + self.written
        
        if self.syl in language.sylfreqs.keys(): #including syllable in language's syllable count
            language.sylfreqs[self.syl] += 1
        else:
            language.sylfreqs[self.syl] = 1

        language.sylcount += 1
        language.allsyls.append(self) #list of all syllables generated
        

class Word:#chooses a number of syllables from the language's list and lists them in order
    def __init__(self, language, wordtype = ''):

        output = []
        fullword = ''
        written = ''
        l = lognormvariate(language.length[0],language.length[1])

        while len(fullword) <= l:

            if len(language.allsyls) < 10000:
                x = Syllable(language)

            else:
                x = choice(language.allsyls)
            
            fullword += x.sounds + '.'
            written += x.written
            output.append(x)

        self.word = output

        self.naive = fullword
        self.written = written.capitalize()

