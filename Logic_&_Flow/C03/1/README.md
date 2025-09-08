# Dictionary Methods

Dictionaries, just like lists, come equipped with a variety of built-in methods to perform common operations. These methods can help you manipulate dictionaries more efficiently. Let's explore some of the key methods:

`keys()`: Returns a view object that displays a list of all the keys in the dictionary.

```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)
# Output: dict_keys(['name', 'age', 'city'])
```

`values()`: Returns a view object that displays a list of all the values in the dictionary.

```python
values = my_dict.values()
print(values)
# Output: dict_values(['Alice', 30, 'New York'])
```

`items()`: Returns a view object that displays a list of a dictionary's key-value tuple pairs.

```python
items = my_dict.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
```

`get(key, default)`: Returns the value for the specified key. If the key is not found, it returns the default value (or `None` if no default is specified).

```python
age = my_dict.get('age')
print(age)
# Output: 30

country = my_dict.get('country', 'USA')
print(country)
# Output: USA
```

`pop(key)`: Removes the element with the specified key and returns its value.

```python
city = my_dict.pop('city')
print(city)
# Output: 'New York'
print(my_dict)
# Output: {'name': 'Alice', 'age': 30}
```

## Quiz

3 Questions

Start

## Challenge

**Easy**

In this challenge, you'll work with a dictionary of student grades to practice essential dictionary operations.

Follow these steps **in order** and use the exact print statements shown:

1. Create a dictionary named `grades` with these initial key-value pairs:
   * "Alice": 85
   * "Bob": 90
   * "Charlie": 78
2. Print all student names and grades using these exact statements:
   * `print("Students:", grades.keys())`
   * `print("Grades:", grades.values())`
3. Add a new student "Diana" with a grade of 92.
4. Use the `get()` method to retrieve Bob's grade and print it using:
   * `print("Bob's grade:", bobs_grade)`
5. Remove "Charlie" from the dictionary using the `pop()` method and then print the updated dictionary using:
   * `print("Updated grades:", grades)`

**Important:** Follow the exact sequence and use the exact print statements shown above to match the expected output.

Expected Output:

```python
Students: dict_keys(['Alice', 'Bob', 'Charlie'])
Grades: dict_values([85, 90, 78])
Bob's grade: 90
Updated grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}
```

[Question](q.py) [solution](solution.py)