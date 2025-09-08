# Iterating Over Strings Part 1

Similar to lists, you can iterate over strings:

```python
text = "Hey"
for char in text:
    print(char)
```

Output:

```python
H
e
y
```

Using index:

```python
for i in range(len(text)):
    print(f"position {i}: {text[i]}")
```

Output:

```python
position 0: H
position 1: e
position 2: y
```

## Challenge

**Easy**

Create a program that receives a string as input, and it prints how many times the character `p` (or P) is in the string.

Some chars might be uppercase, use `char.lower()` to convert it to lowercase.

[Question](q.py) [solution](solution.py)