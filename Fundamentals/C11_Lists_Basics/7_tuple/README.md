# Tuple

A tuple is an immutable (read-only) ordered collection of elements. Unlike lists, once created, tuples cannot be modified.

Create a tuple with parentheses:

```python
fruits = ("apple", "banana", "cherry")
```

You can also create a tuple without parentheses:

```python
colors = "red", "green", "blue"
```

Access tuple elements using indexing (just like lists):

```python
first_fruit = fruits[0]  # "apple"
```

Remember, tuples are immutable, so you cannot modify elements:

```python
# This will cause an error
# fruits[0] = "orange"
```

A tuple with a single element needs a trailing comma:

```python
single_item = ("apple",)  # This is a tuple
not_a_tuple = ("apple")   # This is a string
```