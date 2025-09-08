# Looping Through Dictionaries

Looping through a dictionary allows you to access each key-value pair and perform operations on them. Python provides several ways to iterate through dictionaries, making it easy to work with their contents.

Looping through keys:

```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in my_dict:
    print(key)
```

Output:

```python
name
age
city
```

Looping through values:

```python
for value in my_dict.values():
    print(value)
```

Output:

```python
Alice
30
New York
```

Looping through key-value pairs:

```python
for key, value in my_dict.items():
    print(f'{key}: {value}')
```

Output:

```python
name: Alice
age: 30
city: New York
```

In these examples, the first loop iterates over the keys of the dictionary. The second loop iterates over the values using the `values()` method. The third loop uses the `items()` method to iterate over both keys and values simultaneously.

## Challenge

**Easy**

Create a function named `print_employee_details` that takes a dictionary `employee_data` as an argument. The function should loop through the dictionary and print each key-value pair in the format `'key: value'`. If the dictionary is empty, the function should print `'No data available'`.


[Question](q.py) [solution](solution.py)