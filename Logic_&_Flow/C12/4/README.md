# Recap - Shopping Cart Errors

## Challenge

**Medium**

Create a program that simulates a shopping cart with error handling. Your task is to:

1. Create a function called handle_shopping_cart that processes customer orders
2. The function should accept a list of order strings in the format "item:quantity"
3. Process each order by:
    - Splitting the input string to get the item and quantity
    - Converting the quantity to an integer
    - Adding the item to a shopping cart dictionary with the quantity as value
    - If an item already exists in the cart, update its quantity
4. Handle these specific errors:
    - If the input format is incorrect (missing colon), print "Invalid format: {order}"
    - If the quantity is not a valid number, print "Invalid quantity: {order}"
    - If the quantity is negative, print "Negative quantity not allowed: {order}"
5. Return the completed shopping cart dictionary

[Question](q.py) [solution](solution.py)