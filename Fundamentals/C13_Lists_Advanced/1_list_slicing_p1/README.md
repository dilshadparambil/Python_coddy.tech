# List Slicing Part 1

List slicing allows you to extract portions of a list using the syntax `lst[start:stop]`.

The `slice` operation extracts elements from a starting index (inclusive) to a stopping index (exclusive).

Basic slicing:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
portion = numbers[2:6]
print(portion)
# [2, 3, 4, 5]
```

Omitting start parameter:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
beginning = numbers[:5]
print(beginning)
# [0, 1, 2, 3, 4]
```

When start is omitted, slice begins from index 0.

Omitting stop parameter:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ending = numbers[5:]
print(ending)
# [5, 6, 7, 8, 9]
```

When stop is omitted, slice goes until the end.

## Division Operators

When working with list indices:

- `/` gives you a decimal number (5/2 = 2.5)
- `//` removes the decimal part (5//2 = 2)

For list slicing, use `//` because indices must be whole numbers.

## Challenge

**Easy**

Create a program that receives a list as input (given) and prints the following sliced list (depends on the list length):

- For odd-length lists: take the middle item and one item on each side (3 items total)
- For even-length lists: take the two middle items

[Question](q.py) [solution](solution.py)