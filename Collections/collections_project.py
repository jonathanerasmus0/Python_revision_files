'''We'll build a simple inventory management system for a small store. This system will allow us to add items to inventory, display available items, remove items from inventory, and update the quantity of items.'''

# Define the inventory as a dictionary
inventory = {}

# Function to add items to inventory
def add_item_to_inventory(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

# Function to display available items in inventory
def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Function to remove items from inventory
def remove_item_from_inventory(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"{quantity} {item_name}(s) removed from inventory.")
        else:
            print("Insufficient quantity in inventory.")
    else:
        print("Item not found in inventory.")

# Function to update quantity of items in inventory
def update_item_quantity(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Quantity of {item_name} updated to {new_quantity}.")
    else:
        print("Item not found in inventory.")

# Main function to run the program
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item to Inventory")
        print("2. Display Inventory")
        print("3. Remove Item from Inventory")
        print("4. Update Item Quantity")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity to add: "))
            add_item_to_inventory(item_name, quantity)
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            item_name = input("Enter the name of the item to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            remove_item_from_inventory(item_name, quantity)
        elif choice == '4':
            item_name = input("Enter the name of the item to update: ")
            new_quantity = int(input("Enter the new quantity: "))
            update_item_quantity(item_name, new_quantity)
        elif choice == '5':
            print("Thank you for using the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
