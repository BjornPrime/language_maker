from gen_language import *
import shelve

onset = [u'ʒ','n','d',u'θ',u'ʃ','r','m','k','l','g',u'dʒ','j','s','v','t','f']
medial = [u'ʌ']
nucleus = [u'ɪə',u'ə','a',u'eɪ',u'ɛ',u'aɪ','u',u'ʊ',u'ɪ']
coda = ['n','d',u'θ',u'ʃ','r',u'ʒ','m','k','l','g','t','f']
orthography = {u'eɪ':'ay',u'ʊ':'uy','u':'o','j':'y',u'dʒ':'j',u'ʒ':'zh',u'ʃ':'sh',u'θ':'th',u'ɪə':'i',u'aɪ':'iy',u'ɪ':'y',u'ə':'u',u'ɛ':'e',u'ʌ':'e'}
wordlength = [log(6), 0.2]
clusters = {'g':[0.3,'gr'],'d':[0.2,'dr'],'a':[0.2,'ar','al'],u'ɪə':[0.2,u'ɪər',u'ɪəl'],u'ə':[0.2,u'ər',u'əl']}

sark = Language(onset, medial, nucleus, coda, orthography, wordlength, clusters, structure = [0.99, 0, 1, 0.8], alpha = 0.3)

##y = Syllable(sark)
##print(y.syl)

##final_list = []

for i in range(10000):
    z = Word(sark)

    initial = []

    for item in z.word:
        initial.append(item.positions)
        
    j = 1

    sounds = ''
    glyphs = ''
        
    endings = ['k',u'ʒ',u'ʃ','g','d',u'θ','f']
    endchance = [0.5, 1, 1, 1, 1, 1, 1]

    for item in initial:
        
        if 'coda' in item.keys():

            if item['coda'] in endings and j < len(initial):

                q = endings.index(item['coda'])

                if random() < endchance[q]:

                    del item['coda']
                
            elif item['coda'] in endings:

                q = endings.index(item['coda'])

                if random() < endchance[q]:

                    a = item['coda']
                    b = {'onset':a,'nucleus':u'ʌ'}
                                    
                    initial.append(b)

                    del item['coda']
        
        glyphs += sark.glyphify(item)

        for part in ['onset','nucleus','coda']:

            if part in item.keys():

                sounds += item[part]

        if j < len(initial):

            sounds += '.'

        j += 1

    complete = sounds + ' | ' + glyphs.capitalize()

    ##now to record the word
    
    sark.wordlist.append(complete)

    if complete in sark.wordfreqs.keys():

        sark.wordfreqs[complete] += 1

    else:

        sark.wordfreqs[complete] = 1

    sark.wordcount += 1

sylfreqlist = []
wordfreqlist = []

for item in sark.sylfreqs.keys():
    sylfreqlist.append((item,round(sark.sylfreqs[item]*100/sark.sylcount,2)))

for item in sark.wordfreqs.keys():
    wordfreqlist.append((item,round(sark.wordfreqs[item]*100/sark.wordcount,2)))

commonsyls = sorted(sylfreqlist, key=lambda item: item[1], reverse = True)[0:50]
commonwords = sorted(wordfreqlist, key=lambda item: item[1], reverse = True)[0:50]

print(commonsyls)
print(commonwords)

##### Can't print non-standard characters for some reason??? #####
##
##f = open('sark','w')
##
##f.write('Sark\n----------\n\n')
##
##f.write('Top 50 Syllables\n-----\n')
##
##i = 1
##
##for item in commonsyls:
##
##    f.write('{}. '.format(i) + item[0] + ' (' + str(item[1]) + ')' + '\n')
##
##    i += 1
##
##f.write('\nTop 50 Words\n-----\n')
##
##i = 1
##
##for item in commonwords:
##
##    f.write('{}. '.format(i) + item[0] + ' (' + str(item[1]) + ')' + '\n')
##
##    i += 1
##
##f.close()

g = shelve.open('RPG Languages')

g['Sark'] = sark

copy = g['Sark']

for j in range(10):

    print(choice(copy.wordlist))

g.close()
