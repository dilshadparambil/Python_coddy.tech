# Logical Operators Part 3

In Python, you can combine multiple conditions using logical operators (and, or, not) to create more complex expressions.

Let's create a condition that checks if a number is both positive and even:

```python
number = 6
```

Now let's check if the number is positive:

```python
is_positive = number > 0
```

Let's also check if the number is even:

```python
is_even = number % 2 == 0
```

We can combine these conditions using the `and` operator:

```python
result = is_positive and is_even
```

This evaluates to `True` because 6 is both positive and even.

For a more direct approach, you can combine conditions without intermediate variables:

```python
result = number > 0 and number % 2 == 0
```

Similarly, you can use the `or` operator to check if at least one condition is true:

```python
number = -4
is_negative_or_odd = number < 0 or number % 2 != 0
```

This evaluates to `True` because -4 is negative (even though it's not odd).

## Challenge

**Easy**

Write code that checks if a person is eligible to drive. A person is eligible to drive if ALL of the following conditions are met:

1. The person is at least 18 years old
2. The person has a license
3. The person has insurance

Your program should:

1. Read an integer `age` from the first line of input
2. Read a string `has_license` from the second line of input (either "true" or "false")
3. Read a string `has_insurance` from the third line of input (either "true" or "false")
4. Convert the license and insurance inputs to boolean values
5. Check all three conditions and store the result in a variable named `result`
6. Print the final result (should be `True` or `False`)

[Question](q.py) [solution](solution.py)