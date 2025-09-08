# Nested If - Else

Nested If-Else statements allow you to check multiple conditions by placing one if-else statement inside another.

Create a basic if-else statement:

```python
age = 18
title = "None"
if age >= 18:
    title = "Adult"
else:
    title = "Minor"
```

Now let's add a nested condition inside:

```python
age = 18
title = "None"
allowed_to_drink = False
if age >= 18:
    title = "Adult"
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"
```

In this example, the second if-else only executes when the first condition is `True`.

## Challenge

**Beginner**

Write a program that determines eligibility for a movie based on age and parental guidance.

Your program should:

1. Create a variable `age` and assign it a value from input (**given**).
2. Create a variable `with_parent` and assign it a True/False value from input (**given**).
3. Create a variable named `message` with the value of `"None"` (**given**).
4. Use nested if-else to determine what string to put in `message`: 
   * If age is 18 or older, set `"You can watch any movie"`.
   * If age is under 18: 
      * If with_parent is True, set `"You can watch PG-13 movies"`.
      * If with_parent is False, set `"You can only watch G-rated movies"`.  

[Question](q.py) [solution](solution.py)
