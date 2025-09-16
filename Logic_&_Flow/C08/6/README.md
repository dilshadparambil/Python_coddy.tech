# List by Course

## Challenge

**Easy**  
Create a function named `list_students_by_course` that takes one argument: `course` (string). The function should:

1. Iterate through the `student_records` dictionary and find all students enrolled in the specified course.  
2. Return a list of names of students who are enrolled in the course.  
3. If no students are enrolled in the course, return an empty list.  

Add (replace) the following block of code at the bottom of your code:

```python
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
```

[Question](q.py) [solution](solution.py)