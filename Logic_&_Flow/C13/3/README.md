# Update Stock

## Challenge

**Easy**

Create a function named `update_stock` that takes two arguments: `item` (string) and `quantity` (int). The function should:

1. Check if the item already exists in the `inventory` dictionary.
    - If it does not exist, print 
    `"Error: Item '<item>' not found.".`
2. If the item exists, calculate the new stock by adding the `quantity` to the current stock.
    - If the new stock is negative, print `"Error: Insufficient stock for '<item>'."` and do not update.
    - Otherwise, update the stock in the inventory.
3. Print `"Stock for '<item>' updated successfully."`

Add (replace) the following block of code at the bottom of your code:

```
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)    
```

[Question](q.py) [solution](solution.py)