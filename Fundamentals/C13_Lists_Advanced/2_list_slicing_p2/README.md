# List Slicing Part 2

Slicing has another **step** parameter: `lst[start:stop:step]`.

The step parameter controls how many elements to skip between selections.

Getting every second element:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[1:8:2]
print(result)
# [1, 3, 5, 7]
```

This gets every second element from index 1 to 8.

Getting every third element:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[2::3]
print(result)
# [2, 5, 8]
```

This gets every third element from index 2.

## Negative Indices

Slicing also supports negative indices for counting from the end.

Counting from end:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[-3:]
print(result)
# [7, 8, 9]
```

Here, -3 means "start 3 positions from the end".

Count until end:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[:-2]
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7]
```

Here, -2 means "stop 2 positions from the end" (exclusive).

Reversing with negative step:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[::-1]
print(result)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

- Empty space before first `:` means "start from beginning"
- Empty space between `:` means "go until the end"
- -1 means "move backwards one step at a time"

## Challenge

**Easy**

Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:

- A list containing every third element, starting from index 1 (the second element)
- A list containing all the elements from the 6th element to the 1st in reverse order
- A list containing every second element starting from the middle of the list to the end

[Question](q.py) [solution](solution.py)