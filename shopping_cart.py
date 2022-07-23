from IPython.display import clear_output

# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
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
    new_item = item                                    # I'm creating a variable for the item that I'm about to add (new_item). Since new_item = item, new_item will have all the attributes that I've already set for item.
    item_name = input("What type of item would you like to add? ")          #python predefined funtion (input) will retrieve the information I'm looking for (name)      
    item_name = new_item["name"]                  #I'm telling the computer what to do with item_name. It needs to go into a dictionary. Since "name" a string it's telling my comp that it should be a key within my dictionary that is called new_item.

    item_price = input(f"What is the price of one {item_name}? ") #asking for a price and giving that a variable (item_price)
    item_price = float(item_price)                               #since we don't want a string, we will assume the price is a float and will turn the input into a float.
    item_price += new_item["price"]

    item_quantity = input(f"How many {item_name}'s do you want? ")   #asking another question
    item_quantity = int(item_quantity)                               #input is always going to output a string. Since I'm looking for an integer i need to tell the comp to turn item_quantity into an integer here.
    item_quantity += new_item["quantity"]                            #Two things happening here. I'm telling the comp where to put the information we've just received (item_quantity). Just like name it needs to go into our new_item dictionary as a value that is associated with a key we're calling "quantity". The 2nd thing we're doing here is the +=.  We do this because we might need to add more later.  

    return new_item


while True:
    new_item = create_new_item()
    shopping_cart.append(new_item)
    add_more = input("Would you like to add another item? Y/n " )
    if add_more == "n":
        break
    
print(shopping_cart)


    