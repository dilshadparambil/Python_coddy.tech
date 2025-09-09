# Membership Checks

Membership checks in Python let you check if a value exists in a collection like a list, tuple, set, or dictionary using `in` and `not in`.

The `in` operator checks if a value exists:

```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
```

The `not in` operator checks if a value does not exist:

```python
numbers = [1, 2, 3]
print(4 not in numbers)  # True
```

For dictionaries, membership checks apply to keys by default:

```python
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)  # True
print("Alice" in my_dict)  # False
```

## Challenge

**Easy**

You are given a list of names and a dictionary of student grades. Write a program that:

1. Checks if the name `"Alice"` is in the list.
2. Checks if the name `"David"` is not in the list.
3. Checks if the key `"Bob"` exists in the dictionary.
4. Checks if the key `"Eve"` does not exist in the dictionary.

*Check the test case for the output format!*

[Question](q.py) [solution](solution.py)