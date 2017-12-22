from gen_language import *
import shelve

#establish sounds of the language

onset = ['g',u'tʃ','r','s',u'ð','d','f','k','m','l','b',u'ɲ','n','v','z','p',u'dʒ',u'ʒ','t',u'ʃ','h']
medial = ['g']
nucleus = ['a',u'ɪ',u'ʊ','o',u'iə',u'ɛ']
coda = ['g',u'tʃ','r','s',u'ð','d','f','k','m','l','b','n','v','z','p',u'dʒ',u'ʒ','t',u'ʃ','h']
orthography = {u'ɲ':'ñ',u'dʒ':'j',u'ʒ':'jh',u'tʃ':'c',u'ʃ':'sh',u'ɪ':'i',u'ʊ':'u',u'ɛ':'e',u'iə':'ia'}
wordlength = [log(8), 0.2]

Mitrian = Language(onset, medial, nucleus, coda, orthography, wordlength, structure = [0.9,0,1,0.8])

for i in range(10000): #Make a bunch of words
    new_word = Word(Mitrian)

    print(new_word.naive + '|' + new_word.written)


#save to shelf

g = shelve.open('RPG Languages')

g['Mitrian'] = Mitrian

g.close()
