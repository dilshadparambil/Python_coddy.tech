# Mathematical Operations Part 1

Sets support mathematical operations such as union, intersection, difference, and symmetric difference. These operations are useful for comparing and combining sets in various ways.

Union (`|` or `union()`): Combines the elements from both sets, excluding duplicates.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
# Output: {1, 2, 3, 4, 5}
```

Intersection (`&` or `intersection()`): Returns a set containing only the elements that are common to both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)
# Output: {3}
```

Difference (`-` or `difference()`): Returns a set containing the elements that are in the first set but not in the second set.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)
# Output: {1, 2}
```

Symmetric Difference (`^` or `symmetric_difference()`): Returns a set containing the elements that are in either of the sets, but not in both.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
# Output: {1, 2, 4, 5}
```

## Challenge

**Easy**

Create a function named `set_operations` that takes two sets, `set1` and `set2`, as arguments. The function should perform the following operations:

1. Calculate the union of `set1` and `set2`.
2. Calculate the intersection of `set1` and `set2`.
3. Calculate the difference of `set1` and `set2` (elements in `set1` but not in `set2`).
4. Calculate the symmetric difference of `set1` and `set2`.
5. Return a dictionary containing the results of these operations, with the keys `"union"`, `"intersection"`, `"difference"`, and `"symmetric_difference"`.

[Question](q.py) [solution](solution.py)