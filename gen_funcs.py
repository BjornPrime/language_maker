from random import *
from math import *

class Settlement:
    def __init__(self, name, population, features = [], merchants = []):
        self.name = name
        self.pop = population
        self.feat = features #this is a list of keywords to indicate certain conditions relevant to the generation of the settlement
        self.merch = merchants

def merchants(town):

    pop = town.pop

    if 'Hub' in town.feat: #doubles effective population for wealthier towns
        pop = 2*pop
    
    if 'Arcane' in town.feat:
        magic = 1
    else:
        magic = 0

    merch = [0,0,0,0,0,0]

    i = 0

    for entry in merch:
        l = 10**(6 - i) #pop with 50% chance of that level of shop
        p = (1/2)**(pop/l) #1 - p = probability of shop
        r = random()
        if r >= p:
            j = 1
            while r >= p:
                merch[i] += 1
                r = random()
                p = (1/2)**(pop/(l*(2**j))) #1 - p = chance of another shop at same level
                j += 1
        i += 1

    return merch
    
y = Settlement('Yshyyk', 7045, ['Hub'])
z = merchants(y)

y.merch = z

print(y.merch)
