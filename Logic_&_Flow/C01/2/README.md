# Multiple Variable Assignments

In Python, you can assign values to multiple variables in a single line. This feature can make your code more concise and readable. Let's explore how to use multiple variable assignments effectively.

Basic Multiple Assignments:

```python
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

Assigning the same value to multiple variables:

```python
x = y = z = 10
print(x)  # Output: 10
print(y)  # Output: 10
print(z)  # Output: 10
```

Assigning values from a list:

```python
numbers = [4, 5, 6]
a, b, c = numbers
print(a)  # Output: 4
print(b)  # Output: 5
print(c)  # Output: 6
```

## Challenge

**Easy**

Write a Python program that performs the following tasks:

1. Assign values to three variables `name`, `age`, and `city` in a single line. Set `name` to `"Alice"`, `age` to `30`, and `city` to `"New York"`.
2. Assign the value `100` to three variables `x`, `y`, and `z` in a single line.
3. Create a list named `colors` containing the values `"red"`, `"green"`, and `"blue"`. Assign these values to three variables `color1`, `color2`, and `color3` in a single line.

[Question](q.py) [solution](solution.py)