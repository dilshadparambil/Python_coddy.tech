student_records={}

def add_student(name,age,courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name]={'age':age,'grades':set(),'courses':courses}
        print(f"Student '{name}' added successfully.")

def add_grade(name,grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.") 

def is_enrolled(name,course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]['courses']:
            return True
        else:
            return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        grades_set=student_records[name]['grades']
        if grades_set:
            return float(sum(grades_set)/len(grades_set))
        else:
            return 0

def list_students_by_course(course):
    stud_list=[]
    for student in student_records:
        if course in student_records[student]['courses']:
            stud_list.append(student)
    return stud_list

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list