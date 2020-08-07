# Author: Leon Samuel
# Date: 1.9.20
# Description: An object oriented store that can add items, add costumers, track costumer purchases, and print prices for items that are still available on checkout.

import unittest

class InvalidCheckoutError(Exception):
    pass

class Product:
    """
    creates object for store item using item ID, title, description, price and tracks the remaining quantity of the available items
    """

    def __init__(self, id_code, title, description, price, quantity_available):
        """ creates object for store item based on stated parameters """
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        """ returns current product id code """
        return self._id_code

    def get_title(self):
        """ returns product title """
        return self._title

    def get_description(self):
        """ returns product description """
        return self._description

    def get_price(self):
        """ returns product price """
        return self._price

    def get_quantity_available(self):
        """ returns product quantity available """
        return self._quantity_available

    def decrease_quanity(self):
        """ decreases the available quantity of the store item by 1 """
        self._quantity_available -= 1


class Customer:
    """
    creates a object for each customer using their name, ID, and membership status
    """

    def __init__(self, customer_name, account_ID, premium_member):
        """ creates customer object using provided information """
        self._customer_name = customer_name
        self._account_ID = account_ID
        self._premium_member = premium_member
        self._customer_cart = []

    def get_name(self):
        """ returns customer name """
        return self._customer_name

    def get_account_ID(self):
        """ returns account ID """
        return self._account_ID

    def is_premium_member(self):
        """ returns whether customer is a premium member """
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """ adds product product ID code to the customer's cart"""
        self._customer_cart.append(product_id)

    def get_cart(self):
        """ returns customer's cart"""
        return self._customer_cart

    def empty_cart(self):
        """ empties customer's cart"""
        self._customer_cart = []


class Store:
    """
    creates a store along with applicable methods to use products and members to complete a purchase
    """

    def __init__(self):
        """ initializes blank lists for store's member and inventory """
        self._members = []
        self._inventory = []

    def add_product(self, product_to_add):
        """ adds a product to the inventory """
        self._inventory.append(product_to_add)

    def add_member(self, member_to_add):
        """ adds a customer to the members """
        self._members.append(member_to_add)

    def get_inventory(self):
        """returns inventory"""
        return self._inventory

    def get_product_from_ID(self, id_code):
        """ returns the product with the matching ID. If no matching ID is found, it returns value None """
        for i in self.get_inventory():
            if id_code == i.get_id_code():
                return i.get_title()
            else:
                continue
        return None

    def get_member_from_ID(self, account_id):
        """ returns the Customer with the matching ID. If no matching ID is found, it returns value None """
        for i in self._members:
            if i.get_account_ID() == account_id:
                return i.get_name()
            else:
                continue
        return None

    def product_search(self, search):
        """  return a sorted list of ID codes for every product whose title or description contains the search string. """

        search_results = [] # blank list of items for search to add to

        for i in self.get_inventory():
            if search.lower() in i.get_title().lower(): # makes search case-insensitive
                search_results.append(i.get_id_code())
            else:
                continue

        for i in self.get_inventory():
            if search.lower() in i.get_description().lower() and i.get_id_code() not in search_results: # makes search case-insensitive
                search_results.append(i.get_id_code())
            else:
                continue

        search_results.sort() #sorts list of matched IDs
        return search_results

    def add_product_to_member_cart(self, product_id, member):
        """ adds product product ID code to the customer's cart"""


        for i in self._inventory: #iterating inventory item to add to member cart
            if product_id in [i.get_id_code() for i in self._inventory]:
                if i.get_id_code() == product_id: # checking to see if product ID code matches product ID
                    for r in self._members: #iterating through member objects so we can get ID next
                        if member in [y.get_account_ID() for y in self._members]: #confirm member ID in list of memebers IDs
                            if member == r.get_account_ID(): #because member stores as object
                                if i.get_quantity_available() > 0:
                                    r.add_product_to_cart(product_id)
                                    return "product added to cart"

                                else: #can likely unindent each else by one and get rid of "else" while leaving return since it will execute if nothing found during loops
                                    return "product out of stock"
                            else:
                                continue
                        else:
                            return "member ID not found"
                else:
                    continue
            else:
                return "product ID not found"


    def check_out_member(self, member):
        """ checks member out using items in their cart, provides member with total based on available items and if they are premium member """

        total = 0 #will track total cost as each product is verified as available
        member_IDs = []

        for i in self._members: #iterate through memebers while listing IDs
            member_IDs.append(i.get_account_ID())

        if member not in member_IDs:
            raise InvalidCheckoutError #no member in members with this ID, cannot complete purchase

        for i in self._members: #iterate through member list
            if member == i.get_account_ID(): #confirms which matching member's cart to use
                for r in i.get_cart(): #iterates through cart to get product ID, r == product IDs in member cart
                    for q in self._inventory: # q == product object
                        if r == q.get_id_code(): # if r(productID) matches an ID in inventory
                            if q.get_quantity_available() > 0: #ensures item still in stock
                                total += q.get_price() #totals price as it iterates through
                                q.decrease_quanity()

        for i in self._members:
            if member == i.get_account_ID():
                i.empty_cart() #empties member cart now that they have checked out items


        for i in self._members:
            if member == i.get_account_ID():
                if i.is_premium_member() == False: #def not referencing this right #adding shipping cost for non premium members
                    return total * 1.07


        return total

def main():
    try:
        p1 = Product("48", "Balding Spray", "when a bald spot of the usual size just won't do", 330.45, 2)
        c2 = Customer("Vishnue", "OMG", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c2)
        myStore.add_product_to_member_cart("48", "OMG")
        result = myStore.check_out_member("OG")
    except InvalidCheckoutError:
        print ("Member was not found in system. Please try again.")


if __name__ == '__main__':
    main()




