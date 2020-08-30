import string
import random
class Stats:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def formatIT(self):
        return str(self.name)+' is %d'%self.age+' years old'

    

def GenName():
    from collections import defaultdict
    from random import choice, randint

    starts = []
    middles = defaultdict(list)
    ends = []

    # Read through a list of names
    with open('names.txt', 'r') as infile:
        for name in infile:
            name = name.lower().strip()

            # Keep track of all the beginnings
            starts.append(name[:3])

            # Lookup table of next characters
            for i in range(len(name) - 3):
                middles[name[i:i+2]].append(name[i+2])

            # Keep track of all the endings
            ends.append(name[-2:])

    for _ in range(20):

        # Randomly choose a start of a name
        name = choice(starts)

        # Randomly insert some middle characters based upon what we already have
        for _ in range(randint(0, 2)):
            name += choice(middles.get(name[-2:], ['']))

        # Randomly choose the end of a name
        name += choice(ends)

        # See what we got
        global Name
        Name = name.title()
def GenCar():
    for i in range(500):
        GenName()
        Person = Stats(name = Name,age=random.randint(20,80))
        print(Person.formatIT())

GenCar()
Best_names = []