# Nested Loop

A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

Let's start with a simple nested loop to understand the concept:

```python
# Outer loop
for i in range(3):
    print(f"Outer loop iteration: {i}")
    
    # Inner loop
    for j in range(2):
        print(f"  Inner loop iteration: {j}")
```

When you run this code, you'll see:

```python
Outer loop iteration: 0
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 1
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 2
  Inner loop iteration: 0
  Inner loop iteration: 1
```

Notice that for each iteration of the outer loop, the inner loop completes all of its iterations.

Now let's see a practical example - printing a simple pattern:

```python
# Print a 2x3 rectangle of stars
for row in range(2):  # 2 rows
    line = ""
    for col in range(3):  # 3 columns
        line += "*"
    print(line)

# Output:
# ***
# ***
```

The outer loop controls how many rows we print, and the inner loop builds each row by adding stars.

## Challenge

**Easy**

Write code that prints a rectangle pattern of stars (*) using nested loops.

Your program should:

1. Read two integers: `rows` and `cols`
2. Use a nested loop structure to print the pattern
3. The outer loop should iterate through each row
4. The inner loop should build each row with the correct number of stars
5. Print each completed row

Example: if input is 3 rows and 4 columns, output should be:

```python
****
****
****
```

[Question](q.py) [solution](solution.py)