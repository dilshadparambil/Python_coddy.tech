# Check Availability

## Challenge

**Easy**

Create a function named `check_availability` that takes one argument: `item` (string). The function should:

1. Check if the item exists in the `inventory` dictionary.
    - If it does not exist, return `"Item not found"`.
2. If the item exists, return the current stock of the item.

Add (replace) the following block of code at the bottom of your code:

```
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found" 
```

[Question](q.py) [solution](solution.py)
