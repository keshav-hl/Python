#Iterating over dictionary keys/
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)

#Iterating over dictionary values/
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)

#Iterating over both keys and values/
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")
    