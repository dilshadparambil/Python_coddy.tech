# Top Students

## Challenge

**Easy**

Create a function named `filter_top_students` that takes one argument: `threshold` (float). The function should:

1. Iterate through the `student_records` dictionary and find all students whose average grade is greater than the specified `threshold`.
2. Use the `calculate_average_grade` function to get each student's average grade.
3. Return a list of names of the top students.
4. If no students meet the criteria, return an empty list.

Add (replace) the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
```

Take a moment to reflect on how you've combined dictionaries, sets, and decision-making to create a fully functional program. Great job! 🚀

[Question](q.py) [solution](solution.py)