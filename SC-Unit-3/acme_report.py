#!/usr/bin/env python
from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive',
              'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise',
         'Mousetrap', '???']


def generate_products(n=30):
    '''
    Generates random product list of default quantity = 30
    '''
    product_list = []
    for i in range(n):
        product = Product(random.choice(ADJECTIVES)+' ' +
                          random.choice(NOUNS),
                          random.randint(5, 101),
                          random.randint(5, 101),
                          random.uniform(0.0, 2.5000001))
        product_list.append(product)
    
    return product_list


def inventory_report(products):
    '''
    Prints out nice product report
    '''
    names = []
    prices = []
    weights = []
    flammability = []
    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammability.append(product.flammability)
    unique_names = set(names)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(unique_names))
    print('Average product price: ', sum(prices) / float(len(prices)))
    print('Average product weight: ', sum(weights) / float(len(weights)))
    print('Average product flammability: ', sum(flammability) /
          float(len(flammability)))
    return names

if __name__ == '__main__':
    inventory_report(generate_products())