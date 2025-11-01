# Generate Report

## Challenge

**Hard**


The inventory system already has these components implemented:

1. A global `inventory` dictionary where:
    - Keys are item names (strings)
    - Values are dictionaries containing:
        - `"price"`: The price of the item (float)
        - `"stock"`: Current quantity in stock (integer)
2. An `add_item(item, price, stock)` function that adds new items to inventory
3. An `update_stock(item, quantity)` function that updates the stock level
4. A `check_availability(item)` function that returns the current stock level

Your task is to implement the `sales_report(sales)` function that:

1. Takes a `sales` dictionary where:
    - Keys are item names
    - Values are quantities sold
2. For each item in the sales dictionary:
    - Checks if the item exists in inventory
    - Checks if there's sufficient stock
    - Updates the inventory by reducing stock levels
    - Calculates revenue based on price and quantity sold
3. Returns a formatted string with the total revenue

Handle these specific errors:

- If an item doesn't exist in inventory, print: `"Error: Item '{item}' not found."`
- If there's insufficient stock, print: `"Error: Insufficient stock for '{item}'."`

The output should be a string formatted as: `“Total revenue: ${total:.2f}”`

Add (replace) the following block of code at the bottom of your code:

```
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)

```

[Question](q.py) [solution](solution.py)










