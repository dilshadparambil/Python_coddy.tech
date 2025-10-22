# Handling Multiple Exceptions

In Python, we can handle different types of exceptions in separate `except` blocks. This allows us to respond differently based on the specific error that occurs.

Start with a basic try-except structure:

```python
try:
    # Code that might raise exceptions
    pass
except Exception as e:
    # Handle any exception
    pass
```

To handle multiple exceptions, add specific except blocks:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

You can also catch multiple exception types in a single except block:

```python
try:
    # Some code
    pass
except (ValueError, TypeError):
    print("Invalid input type!")
```

The order of except blocks matters - always place more specific exceptions before more general ones.

## Challenge

**Easy**

Create a function called `process_data` that:

1. Takes a string input representing potential data
2. Tries to convert it to an integer, then calculates 100 divided by that integer
3. Returns the result
4. Handles at least 3 possible exceptions: 
   * `ValueError` if the input cannot be converted to an integer (print "Input must be a number!")
   * `ZeroDivisionError` if the input is 0 (print "Cannot divide by zero!")
   * Any other exception with a generic handler (print "An unexpected error occurred!")
   
[Question](q.py) [solution](solution.py)