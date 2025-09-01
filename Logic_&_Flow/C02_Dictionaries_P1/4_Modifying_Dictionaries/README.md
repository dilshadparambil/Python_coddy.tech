# Modifying Dictionaries

Dictionaries in Python are not static; you can modify them after they are created. You can add new key-value pairs, update existing ones, or delete them.

Adding a new key-value pair:

```python
# Start with an empty dictionary
my_dict = {}

# Add a new key-value pair
my_dict["name"] = "Alice"
my_dict["age"] = 30

print(my_dict)
# Output: {'name': 'Alice', 'age': 30}
```

Updating an existing value:

```python
# Update the age
my_dict["age"] = 31

print(my_dict)
# Output: {'name': 'Alice', 'age': 31}
```

Deleting a key-value pair:

```python
# Delete the age
del my_dict["age"]

print(my_dict)
# Output: {'name': 'Alice'}
```

In these examples, we first add a new key-value pair to an empty dictionary. Then, we update the value of an existing key. Finally, we delete a key-value pair using the `del` keyword.

## Challenge

**Easy**

Create a function named `update_employee_info` that takes three parameters: `employee_dict` (a dictionary), `key` (a string), and `value`. The function should update the `employee_dict` with the new `key` and `value`. If the key already exists, its value should be updated. If the key does not exist, a new key-value pair should be added. The function must return the updated dictionary.

**Important:** Make sure to modify the original dictionary and return it. Use the square bracket notation `dict[key] = value` to add or update entries.

[Question](q.py) [solution](solution.py)