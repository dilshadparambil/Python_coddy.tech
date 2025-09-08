def create_student_dict(name, age, major):
    # Write code here
    dict={
        "name":name, 
        "age":age,
        "major":major
    }
    return dict

print(create_student_dict("Alice", 20, "Computer Science"))