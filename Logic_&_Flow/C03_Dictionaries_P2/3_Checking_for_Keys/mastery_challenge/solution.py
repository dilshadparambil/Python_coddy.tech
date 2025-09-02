def check_inventory(inventory, item):
    # Write code here
    if item in inventory:
        print(f"{item} is in stock. Quantity: {inventory[item]}")

    else:
        print(f"{item} is not in stock.")