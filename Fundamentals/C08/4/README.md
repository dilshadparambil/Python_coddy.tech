# Continue

The `continue` statement stops the current iteration and continues to the next iteration. For example:

```python
for i in range(3, 9):
    if i == 5:
        continue
    print(i)
```

The loop will iterate through the numbers from `3` to `8`, and when it reaches `i=5` it will skip that iteration and continue to the next one. The output is:

```python
3
4
6
7
8
```

Notice, number 5 is not in the output.

## Challenge

**Beginner**

You are given a code which prints the numbers from 1 to 20 (including).

Your task is to add `if` and `continue` statements so that **only the even numbers** will be printed (2, 4, 6, ...).

[Question](q.py) [solution](solution.py)