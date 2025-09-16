# Is Enrolled

## Challenge

**Easy**  
Create a function named `is_enrolled` that takes two arguments: `name` (string) and `course` (string). The function should:  
1. Check if the student name exists in the `student_records` dictionary.  
   * If it does not exist, print `"Student '' not found."` and return `False`.  
2. If the name exists, check if the `course` is in the student's `courses` set.  
   * If it is, return `True`.  
   * If not, return `False`.  

Add (replace) the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(is_enrolled("Alice", "Math"))  # Should return True
print(is_enrolled("Alice", "Biology"))  # Should return False
print(is_enrolled("Bob", "Biology"))  # Should return True
print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return False

[Question](q.py) [solution](solution.py)