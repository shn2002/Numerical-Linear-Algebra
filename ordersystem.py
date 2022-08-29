################################################################################
# Assignment #2 Order System
#
# Purpose: Allows a customer to create an order of items for either take out
# or delivery.
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################

# Understanding the below classes and their relationships is left as part
# of the assignment...

class Order:

    def __init__(self,items):
        self.__items = items

    def __repr__(self):
        order = "\nItems: \n"
        for item in self.__items:
            order += item + "\n"
        return order

class Delivery(Order):

    def __init__(self,items,address):
        super().__init__(items)
        self.address = address

    def __repr__(self):
        order = "\nDelivery order to " + self.address + "\n"
        order += super().__repr__()
        return order

class Takeout(Order):

    def __init__(self,items,ready_time):
        super().__init__(items)
        self.ready_time = ready_time

    def __repr__(self):
        order = "\nTakeout order ready for " + self.ready_time + "\n"
        order += super().__repr__()
        return order

class Item:

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return self.__repr__() + other


class Food(Item):

    def __init__(self,name,grams):
        super().__init__(name)
        self.grams = grams

    def __repr__(self):
        return self.name + " (" + str(self.grams) + "g)"


class Drink(Item):

    def __init__(self,name,volume):
        super().__init__(name)
        self.volume = volume

    def __repr__(self):
        return self.name + " (" + str(self.volume) + "ml)"


class Alcohol(Drink):

    def __init__(self,name,volume,percentage):
        super().__init__(name,volume)
        self.percentage = percentage

    def __repr__(self):
        item = self.name
        item += " (" + str(self.volume) + "ml, "
        item += str(self.percentage) + "%)"
        return item


# The below code that uses the above classes is generally referred to as
# "client code" in many sources you may read in OO programming, for example:
# https://en.wikipedia.org/wiki/Class_(computer_programming)

# Create an inventory of items
inventory = [Food("Pizza", 1200),
             Food("Hamburger", 800),
             Food("Veggie Burger", 700),
             Food("Sandwich", 900),
             Drink("Coca-cola", 355),
             Drink("Water", 500),
             Drink("Orange juice", 355),
             Alcohol("Beer", 500, 5.5),
             Alcohol("Wine", 360, 11.5),
             Item("Napkin"),
             Item("Plate")]

# Create an initially blank list of order items
order_items = []
order = None

# Ask the customer to select various items
done = False
while (not done):
    print("\nSelect any items you wish to purchase: ")
    for i in range(len(inventory)):
        print("(" + str(i) + ") " + inventory[i].name)
    option = input("Enter a selection or f to finish: ")
    if (option == "f"): done = True
    else:
        # remove the item from inventory, add it to the order items
        opt_num = int(option) # convert option to int to use as an index
        order_items.append(inventory[opt_num])
        del inventory[opt_num]

# Ask customer if they want takeout or delivery, create the order accordingly
print("\nWould you like takeout or delivery?")
print("(0) Takeout")
print("(1) Delivery")
option = int(input("Enter a selection: "))
if (option == 0):
    print("\nWhen will you pick up your order?")
    ready_time = input("Enter a time: ")
    order = Takeout(order_items, ready_time)
else:
    print("\nWhere should the order be delivered?")
    address = input("Enter an address: ")
    order = Delivery(order_items, address)

# Output the order
print(order)


