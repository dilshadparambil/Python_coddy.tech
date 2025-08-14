# Logical Operators Part 4

When working with logical expressions, sometimes we need to simplify or rearrange them.

For example, `not` in front of two conditions joined by `and`, can be split into two separate parts. The `and` becomes `or`, and each part gets its own `not`:

`not (A and B)` is the same as `(not A) or (not B)`

For example:

```python
# Let's check if a number is NOT (between 1 and 10)
number = 15

# These two expressions are equivalent:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # True
print(result2)  # True
```

The opposite is also correct: `not (A or B)` is the same as `(not A) and (not B)`

For example:

```python
# Checking if a person is NOT (a student or employed)
is_student = False
is_employed = False

# These two expressions are equivalent:
result1 = not (is_student or is_employed)
result2 = (not is_student) and (not is_employed)

print(result1)  # True
print(result2)  # True
```

## Challenge

**Beginner**

You're helping a pet shop create a system to determine if they can sell a pet to a customer.

initialize the following variables:

* `has_license` with the value `True`
* `has_space` with the value `True`
* `has_experience` with the value `False`

Write the following logical expressions to determine if:

* `can_sell_regular_pet`: Customer needs EITHER a license OR experience, AND must have space
* `can_sell_exotic_pet`: Customer needs BOTH a license AND experience, AND must have space
* `cannot_sell_any_pet`: Customer has NO license AND NO experience, OR has NO space