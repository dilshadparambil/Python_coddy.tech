# The Enumerate Function

The `enumerate()` function allows you to loop through a sequence (like a list, tuple, or string) while keeping track of the index position of each item.

without `enumerate()` we would access both the index and the value the following way:

```python
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

`enumerate()` is a more elegant way to get both index and value:

```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

Both examples will output:

```python
Index 0: apple
Index 1: banana
Index 2: orange
```

## Challenge

**Easy**

Write a program that processes a list of numbers and finds specific indices using the `enumerate()` function.

**Task:** Given a comma-separated list of numbers as input, print a list of the **indices** of numbers that meet either of these conditions:

* The number is below 50, OR
* The number is divisible by 5 (remainder is 0 when divided by 5)

**Example:**

Input: `80,4,99,36,34`

* 80 (index 0): ≥50 but divisible by 5 → include index 0
* 4 (index 1): <50 → include index 1
* 99 (index 2): ≥50 and not divisible by 5 → exclude
* 36 (index 3): <50 → include index 3
* 34 (index 4): <50 → include index 4

Output: `[0, 1, 3, 4]`

[Question](q.py) [solution](solution.py)