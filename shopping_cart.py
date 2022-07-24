from imghdr import what
from IPython.display import clear_output

# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items         <--- So options need to be Add, Remove, View Cart, and Y/n to quit
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity. 


# what would you like to add?
# What is the price of ____?
# how many {items} would you like to add?
# print( {number} of {items} have been added to your card.
    # This means I need to create am empty dictionary with parameters for name of item, price, and quantity
# what would you like to do? add/remove/show/clear/quit


# your current cart:
# -> there are no items in your cart.
# total: $0.00
# Thank you for shopping with us!

shopping_cart = []

def create_new_item():  #create a function 
    item = {                        # I created a dictionary called "item" within the function
        "name" : "",                # name is the name of the new item. We don't know the name yet, so the value is an empty string
        "price" : 0,                # we don't know the price yet, so we are putting it at zero
        "quantity" : 0              # we don't know the quantity yet, so we'll put this at zero also

    }
    new_item = item                                                                ## I'm creating a variable for the item that I'm about to add (new_item). Since new_item = item, new_item will have all the attributes that I've already set for item.                                

    
    item_name = input("What type of item would you like to add? ")          #python predefined funtion (input) will retrieve the information I'm looking for (name)      
    new_item["name"] = item_name                 #I'm telling the computer what to do with the information received in item_name. It needs to go into a dictionary. It should be a key within my (item) dictionary that is now called new_item.

    item_price = input(f"What is the price of one {item_name}? ") #asking for a price and giving that a variable (item_price)
    item_price = float(item_price)                               #since we don't want a string, we will assume the price is a float and will turn the input into a float.
    new_item["price"] += item_price

    item_quantity = input(f"How many {item_name}'s do you want? ")   #asking another question
    item_quantity = int(item_quantity)                               #input is always going to output a string. Since I'm looking for an integer i need to tell the comp to turn item_quantity into an integer here.
    new_item["quantity"] += item_quantity                           #Two things happening here. I'm telling the comp where to put the information we've just received (item_quantity). Just like name it needs to go into our new_item dictionary as a value that is associated with a key we're calling "quantity". The 2nd thing we're doing here is the +=.  We do this because we might need to add more later.  

    return new_item

def show_cart(list_of_items):
    print("Here are the items in your cart: ")
    for item in list_of_items:
        plural = ""
        if item["quantity"] > 1:
            plural = "s"
        
        message = f"{item['quantity']} {item['name']}{plural} : ${item['price']:.2f}"
        print(message)

def calculate_subtotal(item):
    subtotal = item['quantity'] * item['price']
    return subtotal

def calculate_total(list_of_items):
    total = 0
    for item in list_of_items:
        subtotal = calculate_subtotal(item)
        total += subtotal
    return total



def remove_item(list_of_items):

    item_to_remove = input("Which item would you like to remove? ")
    quantity_to_remove = input(f"How many {item_to_remove}'s do you want to remove? ")
    quantity_to_remove = int(quantity_to_remove)
    for item in list_of_items:
        if item_to_remove.lower() == item['name'].lower():
            item['quantity'] -= quantity_to_remove
    
    return(list_of_items)    



   
    

    
    #python predefined funtion (input) will retrieve the information I'm looking for (name)      
    # new_item["name"] == remove_item                                       #telling python to look at the "name" key in the new_item dictionary
    
    # item_quantity = input(f"How many {'item_name'}'s do you want to remove? ")   #asking another question
    # item_quantity = int(item_quantity)                               #input is always going to output a string. Since I'm looking for an integer i need to tell the comp to turn item_quantity into an integer here.
    # new_item["quantity"] -= item_quantity                           #Two things happening here. I'm telling the comp where to put the information we've just received (item_quantity). Just like name it needs to go into our new_item dictionary as a value that is associated with a key we're calling "quantity". The 2nd thing we're doing here is the +=.  We do this because we might need to add more later.  


    # if what_to_do == "show receipt":
    #     # create_new_item()
    #     # shopping_cart.append(new_item)
    #     shopping_cart.append(new_item)
    #     print("Thanks for shopping! Here is your receipt: " )    
    #     print(item_values[0])
    #     what_to_do
    #     # break    #why can't I break here??

while True:
    what_to_do = input("What would you like to do? (add item, remove item, show receipt, or quit): ") 
    new_item = create_new_item()
    shopping_cart.append(new_item)
    show_cart(shopping_cart)
    if add_more == "n":
        break

    # if add_more == "Y".lower():
    #     new_item = create_new_item()
    #     shopping_cart.append(new_item)
    #     add_more = input("Would you like to add another item? Y/n " )
    # else:
    #     what_to_do
    if what_to_do == "show receipt".lower():
        print("Here is your cart breakdown: " )    
        print(shopping_cart)    #<-----here I just want to print the values.
        # break                 # <------ #why can't I break here??

    # if what_to_do == "quit".lower():
    #     print("Thanks for shopping! Here is your receipt: " )    
    #     print(shopping_cart)                                  # <---- Upon quiting the program, prints out a receipt of the items with total and quantity. 
    #                                                                     #I need it to print in a different format. How do I get this to print out in a block format like a real receipt?
  
    

        



#function isn't adding up my new_items. How do I get it to add and print out a total? 
#Did you tell comp that it needs to add them? Yes. Okay, did you tell comp to print the total after adding? No


    