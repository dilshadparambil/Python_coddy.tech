# Basic Operations

Sets come with built-in operations that allow you to perform common set-related tasks efficiently. These operations include adding elements, removing elements, and checking for the presence of elements.

Adding an element to a set:

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}
```

Removing an element from a set: (**raises an error if it does not exist!**)

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# Output: {1, 3}
```

Checking for the presence of an element:

```python
my_set = {1, 2, 3}
print(2 in my_set)
# Output: True
print(4 in my_set)
# Output: False
```

## Challenge

**Easy**

Create a function named `manage_set` that takes three arguments: `set1` (a set), `element_to_add`, and `element_to_remove`. The function should perform the following operations:

1. Add `element_to_add` to `set1`.
2. Attempt to remove `element_to_remove` from `set1`. If the element is not in the set, do nothing.
3. Check if the number 5 is in `set1`. If it is, return the string `"5 is in the set"`. Otherwise, return the string `"5 is not in the set"`.

[Question](q.py) [solution](solution.py)