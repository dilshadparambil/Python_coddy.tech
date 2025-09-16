# Average Grade

## Challenge

**Easy**  
Create a function named `calculate_average_grade` that takes one argument: `name` (string). The function should:

1. Check if the student name exists in the `student_records` dictionary.  
    - If it does not exist, print `"Student '<name>' not found."` and return `None`.  
2. If the name exists, calculate the average of the grades in the student's `grades` set.  
    - If the `grades` set is empty, return `0`.  
    - Otherwise, calculate and return the average grade as a float.  

Add (replace) the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again

[Question](q.py) [solution](solution.py)