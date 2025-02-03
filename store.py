inventory = [
    ("Nintendo Switch 2", 999.99),
    ("BBQ Chips", 3.50),
    ("Pokemon Booster: Flaming Tides", 7.00),
    ("Gaterade", 5.00),
    ("Milk", 4.99),
    ("Advil", 9.99),
    ("Cat Fud", 49.99) 
]
cart = []
while True:
    print("Please select an item to purchase:")
    index = 0
    for name, cost in inventory:
        index = index + 1
        print(f"  {index}. {name}: ${cost}")
    while True:
        user_selection = input("Enter 'C' to checkout or select item number from above: ")
        if(user_selection=='C' or user_selection=='c'):
            break
        user_selection = int(user_selection)
        if(user_selection>len(inventory)):
            print("Please select the items listed Above")
            continue
        cart.append(inventory[user_selection - 1])
    break
    # TODO Exit on checkout
index_cart=0
total=0
for name_cart, cost_cart in cart:
        index_cart = index_cart + 1
        print(f"  {index_cart}. {name_cart}: ${cost_cart}")
        total=total+cost_cart
print("Total is",total)
print("Thank you, come again!")
print(type(inventory))