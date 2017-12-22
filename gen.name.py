from random import *
from math import *

name = ''
initial = ['d','dr','f','fr','g','h','hv','j','k','l','m','n','r','s','sh','t','th','v','y','']
mid = ['a','e','i','o','u','y']
final = ['d','g','k','l','m','n','sh','t','th','']
end = ['d','g','j','k','l','n','th','th','y','']

##class name: ##creates a name
##
##    def __init__(self, lang, purpose = 'place'):
##        self.lang = lang
##        self.purpose = purpose
##
##        if lang == 'Sark':
##            if purpose == 'place':
i = 0

while i < 30:  

    r0 = uniform(1,100) ##random # to determine features of name
    s = ['',''] ## list of syllables

## constructing first syllable
  
    r1 = [uniform(0,100), uniform(0,100), uniform(0,100)] ## range should give each initial equal chance

    x = r1[0]*len(initial)/100 ## initial
    x = floor(x)
    s[0] += initial[x]

    x = r1[1]*len(mid)/100
    x = floor(x)
    if s[0] != mid[x]:
        s[0] += mid[x]

    a = randint(1,4)

    if (mid[x] == 'a' or mid[x] == 'i' or mid[x] == 'u') and a == 4:## approximant placement
        a = randint(1,7)
        if a < 4:
            s[0] += "r"
        elif a < 7:
            s[0] += "l"
        else:
            s[0] += "y"

    x = r1[2]*len(final)/100 ## final
    x = floor(x)
    if final[x] != s[0][-1]:
        s[0] += final[x]

## second syllable
       
    while len(s[0] + s[1]) < 4:
        
        if r0 < 24:
        
            r1 = [uniform(0,100), uniform(0,100), uniform(0,100)]

            x = r1[0]*len(initial)/100 ## initial
            x = floor(x)
            s[1] += initial[x]

            x = r1[1]*len(mid)/100 ##middle
            x = floor(x)
            if s[0] != mid[x]:
                s[1] += mid[x]

            a = randint(1,4)

            if (mid[x] == 'a' or mid[x] == 'i' or mid[x] == 'u') and a == 4:## approximant placement
                a = randint(1,7)
                if a < 4:
                    s[1] += "r"
                elif a < 7:
                    s[1] += "l"
                else:
                    s[1] += "y"

            x = r1[2]*len(final)/100 ## final
            x = floor(x)
            if final[x] != s[1][-1]:
                s[1] += final[x]

        else:
            r2 = randint(1,len(end))
            z = end[r2-1]
            s[1] = z + 'e'

    name = s[0] + s[1]
    name = name.capitalize()
    
##
#### third syllable
##
##    
##    r1 = [uniform(0,100), uniform(0,100), uniform(0,100)]
##
##    x = r1[0]*len(initial)/100 ## initial
##    x = floor(x)
##    s[2] += initial[x]
##
##    x = r1[1]*len(mid)/100
##    x = floor(x)
##    y = mid[x]
##    
##    a = randint(1,4)
##
##    if (mid[x] == 'a' or mid[x] == 'i' or mid[x] == 'u') and a == 4:## approximant placement
##        a = randint(1,7)
##        if a < 4:
##            y += "r"
##        elif a < 7:
##            y += "l"
##        else:
##            y += "y"
##
##    x = r1[2]*len(final)/100 ## final
##    x = floor(x)
##    x = final[x]
##    if x == '':
##        s[2] += 'e'
##    elif (x != y[-1] and s[2] != y):
##        s[2] += y + x
##    else:
##        s[2] += x
##
##    if r0 <= 1:
##        name = s[0] + s[1] + s[2]
##    elif r0 <= 37:
##        name = s[1] + s[2]
##    elif len(s[0]) > len(s[1]):
##        name = s[0]
##    elif len(s[2]) > len(s[1]):
##        name = s[0]
##    else:
##        name = s[1]

    ## no names shorter than 4 letters. How to ensure?

    i += 1

    print (name)
