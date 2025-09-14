# Recap - Tournament Tracker

## Challenge

**Hard**

In a competitive gaming tournament, players participate in different matches. Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:
* `match1`: Players who participated in Match 1
* `match2`: Players who participated in Match 2
* `match3`: Players who participated in Match 3

Your task is to:
1. Find players who participated in all three matches
2. Identify players who participated in exactly two matches
3. Determine players who participated in only one match
4. Count the total number of unique players in the tournament
5. Find players who participated in Match 1 but not in Match 2 or Match 3

Print the results in the following format:
* Use `sorted(list(set_name))` to display players in alphabetical order
* Print the exact output format shown in the example

Example Input:

```python
{"Alice", "Bob", "Charlie", "Diana"}
{"Charlie", "Diana", "Eve", "Frank"}
{"Alice", "Diana", "Frank", "George"}
```

Example Output:

```python
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']
```

[Question](q.py) [solution](solution.py)