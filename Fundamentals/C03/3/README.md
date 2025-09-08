# Arithmetic Shortcuts

Python created a cool shortcut for self-arithmetic operations.

For example, instead of writing:

```python
a = 5
a = a + 3 # a holds 8
```

We can simplify it by writing `+=`:

```python
a = 5
a += 3 # a holds 8
```

The `+=` operator adds the value 3 to `a`.

This operation is valid for all arithmetic operations:

| Operator | Shortcut |
|----------|----------|
| + | += |
| - | -= |
| * | *= |
| / | /= |
| % | %= |

## Challenge

**Beginner**

You are given a code with initialization of `count`. (Don't delete this line!)

Your task is to add the following operations, **in this order**:

1. Add `4` to `count`
2. Multiply `count` by `2`
3. Subtract `1` from `count`

Use the arithmetic shortcuts to do so!  

[Question](q.py) [solution](solution.py)