# Finding Minimum and Maximum

Python offers built-in functions to find the minimum and maximum values in a collection of data, such as a list or a tuple. These functions, `min()` and `max()`, are straightforward to use and can be applied to various data types, including numbers and strings.

Finding the Minimum Value:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
smallest = min(numbers)
print(smallest)
# Output: 1
```

In this example, the `min()` function finds the smallest number in the `numbers` list.

Finding the Maximum Value:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = max(numbers)
print(largest)
# Output: 9
```

Here, the `max()` function finds the largest number in the `numbers` list.

Working with Strings:
The `min()` and `max()` functions can also be used with strings. In this case, they compare the strings based on their lexicographical order (i.e., the order they would appear in a dictionary).

```python
words = ["apple", "banana", "cherry"]
smallest_word = min(words)
largest_word = max(words)
print(smallest_word)
# Output: apple
print(largest_word)
# Output: cherry
```

In this example, `min()` returns `"apple"` because it comes first alphabetically, and `max()` returns `"cherry"` because it comes last alphabetically.

## Challenge

**Easy**

You are given a list of numbers and a list of words. Your task is to write a program that:

1. Finds and prints the smallest and largest number in the list of numbers using `min()` and `max()`.
2. Finds and prints the smallest and largest word in the list of words based on their lexicographical order.

*Check the test cases for output format*

[Question](q.py) [solution](solution.py)