from random import *
from math import *

target = 200000 #target population
size = 300 #minimum settlement size needed to be considered 'urban'

base = 100
mu = 1
sigma = 0.4

group = 'Dwarf' #what race or faction the settlements belong to (Sark, Dwarf)

s = 0 #initialize total settlement count
towns = [] #list of settlements with pop > size

total = 0 #initialize total population count
urban = 0 #initialize total urban poulation count

while total < target:
    x = floor(base ** normalvariate(mu,sigma))
    s += 1
    total += x
    
    if x > size: #check if settlement counts as urban
        
        urban += x
                
        if group == 'Sark':
            
            p = randint(1,147)

            if p < 44:
                p = "Desh"
            elif p < 85:
                p = "Sark"
            elif p < 108:
                p = "Laktan"
            elif p < 126:
                p = "Mirn"
            elif p < 136:
                p = "Yalke"
            elif p < 144:
                p = "Frid"
            else:
                p = "Jurl"

        if group = 'Dwarf':

            p = randint(1,100)
            
            if p < (100 - 2.5*log(x,10)):
                p = "Tidewind"
            else:
                p = "Seaspire"
            
            
            
        towns.append([x, p, s])
        ## print (s, p, x, str(urban/total*100) + "%", len(towns))

towns.sort() ##sort towns list by pop
print (towns)
print("pop = ", total, str(urban/total*100) + "%", len(towns), "towns", s, "settlements")
