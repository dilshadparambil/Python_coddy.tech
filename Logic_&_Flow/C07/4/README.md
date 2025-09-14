# Subsets and Supersets

In set theory, a **subset** is a set where all its elements are contained within another set. Conversely, a **superset** is a set that contains all the elements of another set.

Checking for a subset (`<=` or `issubset()`):

```python
set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1 <= set2
print(is_subset)
# Output: True
```

In this example, `set1` is a subset of `set2` because all elements of `set1` are also in `set2`.

Checking for a proper subset (`<`):

```python
set1 = {1, 2}
set2 = {1, 2, 3}
is_proper_subset = set1 < set2
print(is_proper_subset)
# Output: True
```

Here, `set1` is a proper subset of `set2` because `set1` is a subset of `set2`, and `set2` contains at least one element not in `set1`.

Checking for a superset (`>=` or `issuperset()`):

```python
set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1 >= set2
print(is_superset)
# Output: True
```

In this case, `set1` is a superset of `set2` because `set1` contains all elements of `set2`.

Checking for a proper superset (`>`):

```python
set1 = {1, 2, 3}
set2 = {1, 2}
is_proper_superset = set1 > set2
print(is_proper_superset)
# Output: True
```

Here, `set1` is a proper superset of `set2` because `set1` is a superset of `set2`, and `set1` contains at least one element not in `set2`.

## Challenge

**Easy**

Create a function named `check_sets` that takes two sets, `set1` and `set2`, as arguments. The function should perform the following operations:

1. Check if `set1` is a subset of `set2`.
2. Check if `set2` is a superset of `set1`.
3. Check if `set1` is a proper subset of `set2`.
4. Check if `set2` is a proper superset of `set1`.
5. Return a dictionary containing the results of these operations, with the keys `"is_subset"`, `"is_superset"`, `"is_proper_subset"`, and `"is_proper_superset"`.

[Question](q.py) [solution](solution.py)