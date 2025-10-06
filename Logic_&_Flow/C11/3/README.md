# Lambda Functions Part 2

Lambda functions can also include conditional logic using the `if-else` expression syntax.

Create a basic lambda function with an if-else condition:

```python
# Format: lambda parameters: value_if_true if condition else value_if_false
is_adult = lambda age: "Adult" if age >= 18 else "Minor"
```

Test the lambda function with different values:

```python
print(is_adult(20))  # Output: "Adult"
print(is_adult(15))  # Output: "Minor"
```

You can use more complex conditions as well:

```python
grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"
print(grade_status(75))  # Output: "Pass"
```

## Challenge

**Easy**

Create a lambda function named `categorize_number` that takes a number as an argument and returns:
* "Positive" if the number is greater than 0
* "Zero" if the number is equal to 0
* "Negative" if the number is less than 0

Then use this lambda function to categorize a number received from input.

[Question](q.py) [solution](solution.py)