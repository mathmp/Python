item = None
price = None
list_item = []
list_price = []
total = 0

print("\nWelcome to the Shopping Cart Program!\n")

while item != 5:

    print("\nPlese select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    item=int(input("\nPlease enter an action: "))

    if item == 1:
     item = input("\nWhat item would you like to add? ")
     price = float(input(f"What is the price of {item}? "))
     total = total + price
     print(f"{item} has been added to the cart.\n")

     list_item.append(item)
     list_price.append(price)

    elif item == 2:
     print("The contents of the shopping cart are:")
     for i in range(len(list_item)):
      items = list_item[i]
      prices = list_price[i]
      print(f"{i+1}. {items} ${prices:.2f}")
    
    elif item == 3:
      i = int(input("Wich item would you like to remove? ")) -1
      if 0 <= i < len(list_item):
            removed_item = list_item.pop(i)
            removed_price = list_price.pop(i)
            total -= removed_price
            print(f"{removed_item} has been removed from the cart.")
        
      else:
        print("Sorry, that is not a valid number.")
    
    elif item == 4:
      print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    else:
      print("Action inexistent\n")
    
print("Thank you. Goodbye.")
      
    
      
