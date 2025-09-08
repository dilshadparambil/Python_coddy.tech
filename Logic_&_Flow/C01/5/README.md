# Round Numbers

The `round()` function rounds numbers to the nearest value.

```python
round(number, ndigits)
```

* `number`: The value to round.
* `ndigits`: Decimal places to keep (optional).

Examples:

```python
print(round(4.567))     # 5
print(round(4.567, 2))  # 4.57
print(round(456.78, -1))  # 460
```

Python rounds halfway cases to the nearest even number:

```python
print(round(2.5))  # 2
print(round(3.5))  # 4
```

## Challenge

**Easy**

Write a program that:

1. Takes a number as input from the user (float).
2. Takes the number of decimal places to round to (integer).
3. Outputs the rounded number.

[Question](q.py) [solution](solution.py)