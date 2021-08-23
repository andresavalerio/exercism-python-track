from itertools import product
from random import shuffle
from string import ascii_uppercase

letters = [''.join(pair) for pair in product(ascii_uppercase, ascii_uppercase)]
numbers = [str(i).zfill(3) for i in range(1000)]
allnames = [let + num for let, num in product(letters, numbers)]
shuffle(allnames)
names = iter(allnames)

class Robot:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.name = next(names)