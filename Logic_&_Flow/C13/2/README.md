# Add Item

## Challenge

**Easy**

Create a function named `add_item` that takes three arguments: `item` (string), `price` (float), and `stock` (int). The function should:

1. Check if the item already exists in the `inventory` dictionary.
    - If it does, print 
    `"Error: Item '<item>' already exists.".`
2. If the item does not exist, add it to the inventory with the provided price and stock.
    - Store the price as a float and the stock as an integer.
3. Print `"Item '<item>' added successfully.".`

Add (replace) the following block of code at the bottom of your code:

```
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)  
```

[Question](q.py) [solution](solution.py)