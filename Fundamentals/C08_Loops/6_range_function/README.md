# The Range Function

The `range()` function in Python generates a sequence of numbers, which is commonly used with `for` loops to repeat code a specific number of times.

Create a range that starts at 0 and ends at 4:

```python
for i in range(5):
    print(i)
```

This will output:

```python
0
1
2
3
4
```

You can also specify a start value:

```python
for i in range(2, 6):
    print(i)
```

This will output:

```python
2
3
4
5
```

And you can specify a step value (increment):

```python
for i in range(1, 10, 2):
    print(i)
```

This will output:

```python
1
3
5
7
9
```

## Challenge

**Beginner**

Write a for loop that prints numbers using the `range()` function. Your program should:

1. Read three numbers as input: `start`, `end`, and `step`
2. Use a for loop with `range(start, end, step)` to print all numbers from `start` to `end` (not including `end`) with the given `step` increment
3. Print each number on a new line

**Instructions:**

* The input reading code is already provided
* Replace the comment with your for loop
* Use `range(start, end, step)` in your loop