from imghdr import what
from IPython.display import clear_output

# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items         <--- So options need to be Add, Remove, View Cart, and Y/n to quit
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity. 


shopping_cart = []

def create_new_item():  #create a function 
    item = {                        # I created a dictionary called "item" within the function
        "name" : "",                # name is the name of the new item. We don't know the name yet, so the value is an empty string
        "price" : 0,                # we don't know the price yet, so we are putting it at zero
        "quantity" : 0              # we don't know the quantity yet, so we'll put this at zero also

    }
    new_item = item                                                                ## I'm creating a variable for the item that I'm about to add (new_item). Since new_item = item, new_item will have all the attributes that I've already set for item.                                

    item_name = input("\nWhat type of item would you like to add? ")          #python predefined funtion (input) will retrieve the information I'm looking for (name)      
    new_item["name"] = item_name                 #I'm telling the computer what to do with the information received in item_name. It needs to go into a dictionary. It should be a key within my (item) dictionary that is now called new_item.

    item_price = input(f"\nWhat is the price of one {item_name}? $") #asking for a price and giving that a variable (item_price)
    item_price = float(item_price)                               #since we don't want a string, we will assume the price is a float and will turn the input into a float.
    new_item["price"] += item_price
    # if item_price.isnumeric() != True:
    #     print("Please type a number. For example 2 instead of 'two'")

    item_quantity = input(f"\nHow many {item_name}'s do you want? ")   #asking another question
    item_quantity = int(item_quantity)                               #input is always going to output a string. Since I'm looking for an integer i need to tell the comp to turn item_quantity into an integer here.
    new_item["quantity"] += item_quantity
    
    clear_output()
                              
    added_message = (f"\nThank you! {item_quantity} {item_name}(s) have been added to your cart.")
    print(added_message)
    return new_item

def show_cart(list_of_items):
    for item in list_of_items:
        plural = ""
        if item["quantity"] > 1:
            plural = "s"
        message = f"\n{item['quantity']} {item['name']}{plural} - ${item['price']:.2f} each"
        print(message)
        
def cart_breakdown(list_of_items):
    for item in list_of_items:
        plural = ""
        if item["quantity"] > 1:
            plural = "s"
        subtotal = calculate_subtotal(item)
        message = f"\n{item['quantity']} {item['name']}{plural} - ${subtotal:.2f}"
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

    item_to_remove = input("\nWhich item would you like to remove? ")
    quantity_to_remove = input(f"\nHow many {item_to_remove}'s do you want to remove? ")
    quantity_to_remove = int(quantity_to_remove)
    for item in list_of_items:
        if item_to_remove.lower() == item['name'].lower():
            item['quantity'] -= quantity_to_remove
    print(f"\nThank you! {quantity_to_remove} {item_to_remove}(s) removed from cart")

    return(list_of_items)

       
# def prevent_negatives(list_of_items):
#     for item in list_of_items:
#         subtotal = item['quantity'] * item['price']
#         if subtotal < 1:
#             subtotal = 0
#     return subtotal


while True:
    what_to_do = input("\nWhat would you like to do? (add item, remove item, show cart, or quit): ")

    if what_to_do == "add item".lower():
        new_item = create_new_item()
        shopping_cart.append(new_item)

    elif what_to_do == "remove item".lower():
        remove_item(shopping_cart)
        calculate_subtotal(new_item)

    elif what_to_do == "show cart".lower():
        print("\nHere are the items in your cart: ")
        show_cart(shopping_cart)
        # prevent_negatives(shopping_cart)
        print(f"\nCurrent total: ${calculate_total(shopping_cart):.2f}")

    elif what_to_do == "quit".lower():
        print("\nThanks for shopping with us!")
        cart_breakdown(shopping_cart)
        print(f"\nYour total is ${calculate_total(shopping_cart):.2f}")

        break
    
    else:
        print("\nSorry! that's not a valid response. Please choose from the following options: ")
  

    