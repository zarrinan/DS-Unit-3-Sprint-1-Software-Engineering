#!/usr/bin/env python
import numpy as np


class Product:
    '''
    A class for any product Acme corporation sells 
    '''
    def __init__(self, name: str, price: int=10, weight: int=20,
                 flammability: float=0.5, identifier:
                 int=np.random.uniform(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            print('Not so stealable...')
        elif 0.5 <= self.price / self.weight < 1:
            print('Kinda stealable.')
        else:
            print('Very stealable!')
  
    def explode(self):
        if self.flammability * self.weight < 10:
            print('...fizzle.')
        elif 10 <= self.flammability * self.weight < 50:
            print('...boom!')
        else:
            print('...BABOOM!!')


class BoxingGlove(Product):
    '''
    A subclass of the Product class
    '''
    def __init__(self, name: str, price: int=10, weight: int=10,
                 flammability: float=0.5, identifier:
                 int=np.random.uniform(1000000, 10000000)):
        super().__init__(self)  
        self.weight = weight

    def explode(self):
        print("...it's a glove.")
    
    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif 5 <= self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')
