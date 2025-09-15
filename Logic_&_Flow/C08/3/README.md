# Add Grade

## Challenge

**Easy**

Create a function named `add_grade` that takes two arguments: `name` (string) and `grade` (integer). The function should:

1. Check if the student name exists in the `student_records` dictionary.
   * If it does not exist, print `"Student '<name>' not found."`.
2. If the name exists, add the `grade` to the student's `grades` set.
3. Print `"Grade <grade> added for student '<name>'."`.

Add (replace) the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)
```

[Question](q.py) [solution](solution.py)