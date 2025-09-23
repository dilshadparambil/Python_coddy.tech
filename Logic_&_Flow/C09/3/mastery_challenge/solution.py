def analyze_grades(grades):
    # Write code here
    dict_1={
    'average' : sum(grades.values())/len(grades),
    'highest' : max(grades.values()),
    'lowest' : min(grades.values()),
    'top_student' : max(grades,key=grades.get),
    'bottom_student' : min(grades,key=grades.get),
    }
    return dict_1

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)