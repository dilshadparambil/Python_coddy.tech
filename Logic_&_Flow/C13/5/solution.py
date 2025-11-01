inventory={}

def add_item (item,price,stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item]={'price':float(price),'stock':int(stock)}
        print(f"Item '{item}' added successfully.")

def update_stock (item,quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        new_stock=inventory[item]['stock']+quantity
        if new_stock<0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]['stock']=new_stock
            print(f"Stock for '{item}' updated successfully.")

def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]['stock']

def sales_report(sales):
    total=0
    for item,quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            if quantity>check_availability(item):
                print(f"Error: Insufficient stock for '{item}'.")
            else:
                inventory[item]['stock']-=quantity
                total+=(inventory[item]['price'] * quantity)
    return f"Total revenue: ${total:.2f}"



add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)