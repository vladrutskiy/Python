# adding a login functionality to this shop
import login_function

# triggering login
login_function.check_credentials("1", "2")

# the shop functionality

# the inventory (should be refactored as a separate file)
inventory=[
    ("milk", 4.99),
    ("bread", 3.5),
    ("cottage cheese", 6.02),
    ("Sega Mega Drive 2", 99.99),
    ("Apple gift card", 50.00),
    ("New year tree", 85.75),
    ("PS 5", 699.99),
    ("Google gift card", 25.00)
]

cart = []



def display_inventory():
    """Displays the list of items in the inventory."""
    print("\n Please select an item to purchase:")
    for index, (name, cost) in enumerate(inventory, start=1):
        print(f"  {index}. {name}: ${cost:.2f}")

def get_user_selection():
    """Prompts the user to select an item or checkout."""
    while True:
        user_selection = input("Enter 'C' to checkout or select item number from above: ")
        if user_selection.lower() == 'c':
            return 'C'
        try:
            user_selection = int(user_selection)
            if 1 <= user_selection <= len(inventory):
                return user_selection
            else:
                print("Please select a valid item number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number or 'C' to checkout.")

def add_to_cart(item_index):
    """Adds the selected item from inventory to the cart."""
    item = inventory[item_index - 1]
    cart.append(item)

def checkout():
    """Displays the items in the cart and the total."""
    total = 0
    print("\nYour cart contains:")
    for index, (name, cost) in enumerate(cart, start=1):
        print(f"  {index}. {name}: ${cost:.2f}")
        total += cost
    print(f"\nTotal: ${total:.2f}")
    print("Thank you, come again!")

def main():
    
    """Main function to run the shopping experience."""
    display_inventory()  # Show the inventory list once at the start

    while True:
        user_selection = get_user_selection()

        if user_selection == 'C':  # Checkout if user selects 'C'
            checkout()
            break
        else:
            add_to_cart(user_selection)  # Add item to the cart

# Run the main shopping experience
main()