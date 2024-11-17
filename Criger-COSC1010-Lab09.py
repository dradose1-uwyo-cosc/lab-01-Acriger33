# Ashley Criger
# UWYO COSC 1010
# Submission Date: 11/17/24
# Lab 09
# Lab Section: 10
# Sources, people worked with, help given to: Kaylee Esgar and TAs
# Used ChatGPT4.0. I needed help with printing the reciept and how to get it to read the toppings. I found .strip was needed for 
# the toppings and that helped a lot. I just wasn't thinking of the right way to go about the reciept. I didn't know if it should 
# its own oject and once ChatGPT showed me the direction to go about it, it made a lot more sense. 

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizza:
    def __init__(self, size, sauce = "red"):
        self.setsize(size)
        self.sauce = sauce
        self.toppings = ["cheese"] # Initially has a default cheese
    def setsize(self, size):
        if not size.isdigit() or int(size) < 10:
            self.size = 10
        else:
            self.size = int(size)
    def getsize (self):
        return self.size
    def getsauce(self):
        return self.sauce
    def setsauce(self, sauce):
        self.sauce = sauce
    def getToppings(self):
        return self.toppings
    def setToppings(self, newToppings):
        for t in newToppings:
            self.toppings.append(t)
    def getToppingscount(self):
        return len(self.toppings)

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0 # Initializes a objects (orders and pizzas). Orders will start counting at 0
        self.pizzas=[] # Will start an empty list to add pizzas ordered

    def placeOrder(self): # Starts the process to place an order
        print("Would you like to place an order? exit to exit") # Asks the user if they would like to place an order
        size = input("Please enter the size of the pizza, as a whole number. The smallest size is 10: ") # Asks the user for a size
        while not size.isdigit() or int(size) < 10: # If the size is not a number greater then 10 it will prompt the user to input a different size
            print("Invalid size. Please enter a number 10 or greater")
            size = input("Please enter the size of pizza.")

        sauce = input("What kind of sauce would you like? Leave blank for red sauce: ") # Asks the user what sauce to add
        if not sauce.strip(): # If no sauce is added it will add red sauce automatically
            sauce = "red"
        
        print("Please enter the toppings you would like, leave blank when done: ") # Asks what toppings to add
        toppings = [] # Creates an empty list to add toppings to
        while True: 
            topping = input() # Will add toppings until the user doesnt input anything
            if not topping.strip(): # Breaks when the user doesn't enter anything
                break
            toppings.append(topping.strip()) # Adds the toppings to the list
        
        pizza = Pizza(size,sauce)
        pizza.setToppings(toppings) # Add toppings
        self.pizzas.append(pizza) # Add pizza to the list of orders

        self.orders += 1 # Increases the orders count by 1
        self.getReceipt(pizza) # Gets a receipt for the current pizza order
    def getPrice(self,pizza): # Calculates the price of the pizza
        size_price = pizza.getsize() * Pizzeria.price_per_inch # Gets pizza size and mulitplies it by price per inch to find price of size of pizza
        topping_price = pizza.getToppingscount() * Pizzeria.price_per_topping # Gets topping count and mulitplies it by cost of topping to get topping price
        total_price = size_price + topping_price # Adds the two prices together to get final price
        return size_price, topping_price, total_price # Will show the size price, topping price, and final price
    
    def getReceipt(self,pizza): # Gets a receipt for the pizza
        size_price, topping_price,total_price = self.getPrice(pizza) # Displays the size, sauce, and toppings with a price breakdown
        
        print("\nReceipt:") # Prints Receipt at the top
        print(f"You ordered a {pizza.getsize()}\" pizza with {pizza.getsauce()} sauce and the following toppings:") # Prints what was ordered
        for topping in pizza.getToppings():
            print(f"  - {topping}")
        print(f"Pizza size price: ${size_price:.2f}") # Prints the size price
        print(f"Price for {pizza.getToppingscount()} topping(s): ${topping_price:.2f}") # Prints the topping price and for how many toppings were added
        print(f"Total price: ${total_price:.2f}\n") # Prints the total price

    def getNumberOfOrders(self):
        return self.orders # Returns the number of orders placed


my_pizzeria = Pizzeria() # Will run the pizzeria class
while True:
    user_input = input("Would you like to place an order? Type 'exit' to exit: ").strip().lower()
    if user_input == 'exit': # If exit is typed it will end the code
        print("Thank you!")
        break
    elif user_input == "yes": # If yes the code will ask for an order to be placed
        my_pizzeria.placeOrder()
    else:
        print("Invalid input. Please type 'yes' to order or 'exit' to quit.")

print(f"\nTotal orders placed: {my_pizzeria.getNumberOfOrders()}") # Adds up how many orders were placed

