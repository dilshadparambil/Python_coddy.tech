# Sequence Operators

Python provides several operators that can be used with sequences like lists, strings, and tuples.

Concatenation with the `+` operator joins two sequences together:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
```

After executing the above code, `combined_list` contains:

```python
[1, 2, 3, 4, 5, 6]
```

Repetition with the `*` operator repeats a sequence a specified number of times:

```python
numbers = [1, 2, 3]
repeated_numbers = numbers * 3
```

After executing the above code, `repeated_numbers` contains:

```python
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

These operators work with other sequences too:

```python
# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
stars = "*" * 5  # "*****"
```

## Challenge

**Easy**

Create a function named `create_pattern` that takes two arguments:

* A list of numbers (`numbers`).
* An integer (`repeats`).

The function should:

1. Concatenate the list with itself (list + list).
2. Repeat the resulting list `repeats` times using the `*` operator.
3. Return the final pattern.

[Question](q.py) [solution](solution.py)