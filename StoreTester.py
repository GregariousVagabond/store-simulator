# Author: Leon Samuel
# Date: 1.9.20
# Description: Unit tester for Store file


import unittest

from Store import Product, Customer, Store, InvalidCheckoutError

class StoreTester(unittest.TestCase):
    """
    Contains unit tests for different parts of Store
    """

    def test_1(self):
        """"tests to see if product not added to store remains not in store"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("48", "Balding Spray", "when a bald spot of the usual size just won't do", 330.45, 2)
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        self.assertNotIn(p2, myStore._members)

    def test_2(self):
        """"tests to see if product quantity is not altered"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        self.assertAlmostEqual(p1.get_quantity_available(), 8)

    def test_3(self):
        """"tests to see if customer is added to Store members"""
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_member(c1)
        self.assertIn(c1, myStore._members)

    def test_4(self):
        """"tests to see if product is added to store"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        myStore = Store()
        myStore.add_product(p1)
        self.assertIn(p1, myStore._inventory )

    def test_5(self):
        """"tests to see if get account ID returns correct account ID"""
        c1 = Customer("Yinsheng", "QWF", False)
        result = c1.get_account_ID()
        self.assertIs(result,"QWF")

if __name__ == '__main__':
    unittest.main()