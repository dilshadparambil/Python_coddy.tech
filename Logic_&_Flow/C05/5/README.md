# Recap - Vacation Filter

## Challenge

**Easy**

Write a program that checks if a vacation package meets a customer's requirements.

Your program should:

1. Take the following inputs:
   * `destination`: The vacation destination (a string)
   * `price`: The package price (a float)
   * `nights`: Number of nights included (an integer)
   * `family_preference`: Whether customer wants family-friendly (a boolean)
   * `package_family_friendly`: Whether package is family-friendly (a boolean)
2. Evaluate if the package is suitable based on these conditions:
   * Destination must be "Hawaii" or "Bahamas"
   * Price must be less than $2000
   * Package must include at least 4 nights
   * Family-friendliness must match customer's preference
3. Print the result:
   * "Package is suitable" if all conditions are met
   * "Package is not suitable" if any condition is not met

Note: For boolean inputs, enter 1 for True and 0 for False.

Example Input:

```python
destination = "Hawaii"
price = 1800
nights = 5
family_preference = True
package_family_friendly = True
```

Example Output:

```python
Package is suitable
```

[Question](q.py) [solution](solution.py)