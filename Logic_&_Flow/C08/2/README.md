# Add Student

## Challenge

**Easy**

Create a function named `add_student` that takes three arguments: `name` (string), `age` (integer), and `courses` (a list of strings). The function should:

1. Check if the student name already exists in the `student_records` dictionary. If it does, print `"Student '<name>' already exists."`.
2. If the name does not exist, add it to `student_records` with `age`, an empty set for `grades`, and a set of `courses`.
3. Print `"Student '<name>' added successfully."`.

Add the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
```

[Question](q.py) [solution](solution.py)