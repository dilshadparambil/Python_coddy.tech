# Pattern Finder

## Challenge

**Medium**

Create a function named `find_occurrences` that:

1. Takes two string arguments: `text` and `pattern`
2. Counts how many times `pattern` appears in `text`, including overlapping occurrences
3. Returns a tuple containing:
   * A boolean indicating if the pattern was found (True/False)
   * The number of occurrences of the pattern
   * A list of starting positions where the pattern was found

For example, if `text` is "abababab" and `pattern` is "aba", your function should return `(True, 3, [0, 2, 4])`, since "aba" appears at positions 0, 2, and 4.

If the pattern is not found, return `(False, 0, [])`.

[Question](q.py) [solution](solution.py)
