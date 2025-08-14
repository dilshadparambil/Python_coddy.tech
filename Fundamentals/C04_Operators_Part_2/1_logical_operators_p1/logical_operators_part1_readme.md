# Logical Operators Part 1

Logical operators are used to combine conditional statements.

Python has three logical operators:

* `and`
* `or`
* `not`

Let's see how the `and` operator works:

The `and` operator returns `True` if both statements are true.

```python
# Create two boolean variables
x = True
y = True

# Check if both x and y are True
result = x and y
```

After executing the above code, `result` contains:

```python
True
```

If one of the values is `False`, the result will be `False`:

```python
# Create two boolean variables
x = True
y = False

# Check if both x and y are True
result = x and y
```

This gives us:

```python
False
```

## Challenge

**Easy**

Complete the code to determine if a person is eligible to drive based on their age and license status.

A person is eligible to drive when:

* They are at least 18 years old AND
* They have a valid driving license

Fill in the blanks with the correct values:

1. Fill in the age variable with 20
2. Fill in the has_license variable with True
3. Fill in the minimum age requirement in the comparison