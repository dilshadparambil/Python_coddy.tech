# Break

The `break` statement stops the loop instantly when it's encountered.

For example,

```python
for i in range(10): 
    if i == 6:
        break
    print(i)
```

In the following example the loop iterates regularly until it reaches number 6. Then the program enters the `if` statement and executes the `break` statement. This **exits** the loop immediately. The output is:

```python
0
1
2
3
4
5
```

## Challenge

**Beginner**

You are given a code that prints the numbers from 1 to 10 (including).

Your task is to add `if` and `break` statements so that only the numbers from 1 to 5 will be printed, the loop will exit before printing the numbers from 6 to 10.

[Question](q.py) [solution](solution.py)