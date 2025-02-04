"""An example of how to create a command line selection process for a fictional storefront."""

_inventory = [
    ("Nintendo Switch 2", 999.99),
    ("BBQ Chips", 3.50),
    ("Pokemon Booster: Flaming Tides", 7.00),
    ("Gaterade", 5.00),
    ("Milk", 4.99),
    ("Advil", 9.99),
    ("Cat Fud", 49.99)
]
_cart = []


def get_inventory():
     return _inventory

def print_inventory(inventory: list[tuple[str, float]]) -> float:
    """Prints a list of inventory to the console

    Args:
        inventory (list[tuple[str, float]]): List of items to print.
    """
    index = 0
    total = 0
    for name, cost in inventory:
        index = index + 1
        print(f"  {index}. {name}: ${cost}")
        total= total + cost
    return total


def get_selection(inventory: list[tuple[str, float]]) -> tuple[str, float] | None:
     while True:
        user_selection = input("Enter 'C' to checkout or select item number from above: ")
        if user_selection == "c" or user_selection == "C":
            return None
        elif(int(user_selection) <= len(inventory)):
            return inventory[int(user_selection) - 1]
        else:
            print("Invalid input")
        
def add_item_to_cart(item):
     _cart.append(item)    



# Prompt user to enter selection
print("Please select an item to purchase:")

# Print the inventory
print_inventory(get_inventory())

while True:
    # Get the user's choice
    selection = get_selection(get_inventory())

    if selection is None:
        break
    
    add_item_to_cart(selection) 

cart_total = print_inventory(_cart)
print("Total is ",cart_total)
print("Thank you, come again!")










