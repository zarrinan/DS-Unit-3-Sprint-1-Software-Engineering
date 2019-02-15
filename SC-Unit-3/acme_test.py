#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        '''Test default weight being 20'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
        '''Test default flammability'''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        test_product_list = generate_products()
        self.assertEqual(len(test_product_list), 30)
        
    def test_legal_names(self):
        test_names = inventory_report(generate_products())
        test_names_adjectives = []
        test_names_nouns = []
        for name in test_names:
            test_names_adjectives.append(name.split(' ')[0])
            test_names_nouns.append(name.split(' ')[1])
        for adj in test_names_adjectives:    
            self.assertTrue(adj in ADJECTIVES)
        for nn in test_names_nouns:
            self.assertTrue(nn in NOUNS)
if __name__ == '__main__':
    unittest.main()