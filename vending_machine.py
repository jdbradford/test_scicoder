# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 09:29:39 2014

@author: aphearin
"""

class Item(object):
    def __init__(self,name=None,price=None,quantity=0):
        self.price=price
        self.name=name
        self.quantity=quantity


class VendingMachine(object):
    def __init__(self):
        # VendingMachine.inventory is a dictionary of Item objects
        # the keys to VendingMachine.inventory specify the item names
        self.inventory=dict()

    
    def vend(self,item_name):
        if (item_name in self.inventory.keys()):
            if (self.inventory[item_name].quantity > 0):
                self.inventory[item_name].quantity = self.inventory[item_name].quantity - 1
                print("Enjoy your "+item_name+'!')
            else:
                print("Machine is all out of your selection")
        else:
            print("Sorry, we do not carry your item")
            

    def restock(self,item_name,new_price=None,quantity_to_add=0):
        if (item_name not in self.inventory.keys()):
            if (new_price == None):
                print("All new items added to inventory must be priced")
            else:
                new_item = Item(item_name,new_price,quantity_to_add)
                self.inventory[item_name] = new_item
        elif (item_name in self.inventory.keys() and quantity_to_add >= 0):
            self.inventory[item_name].quantity = self.inventory[item_name].quantity + quantity_to_add
            if (new_price is not None):
                self.inventory[item_name].price = new_price
        else:
            print("Cannot restock a negative number of items")


      
print ''
vm = VendingMachine()

vm.restock("pear",new_price=1.5,quantity_to_add=15)
vm.restock("Mars",new_price=2.5,quantity_to_add=10)

vm.vend("pear")

