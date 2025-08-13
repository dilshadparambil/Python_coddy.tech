# Modulo Operator

The modulo operator `%` tells you what's left over after dividing one number by another.

```python
result = dividend % divisor
```

* **dividend:** The number being divided.
* **divisor:** The number that divides the dividend.
* **result:** The remainder of the division.

For example

```python
result = 10 % 3
```

Here, 10 is divided by 3. 3 goes into 10 three times, with a remainder of 1. So, `result` will be 1.

Usually modulo is used for checking if a number is even or odd:

* If a number is even, dividing it by 2 will leave a remainder of 0.
* If a number is odd, dividing it by 2 will leave a remainder of 1.

## Challenge

**Beginner**

Write a code that initializes three variables, `a`, `b` and `c` with the values `9`, `2`, and `11` (respectively).

After that, initialize the following variables:

* `d` that will hold the result of `a` modulo `2` 
* `e` that will hold the result of `b` modulo `3`
* `f` that will hold the result of `c` modulo `10`

Check out the result and see how different dividends and divisors affect the result.  

[Question](q.py) [solution](solution.py)