#Example-01/---
attendence = 75
if_teacher_frd = True

if attendence >=75:
    print("You can enter to exam...")
elif if_teacher_frd:
    print("You can enter to exam...")
else:
    print("You can't enter to exam...")

#easyer way of above code with logical operations/
#first - Example/
attendence = 50
if_teacher_frd = True

if attendence >= 75 or if_teacher_frd:
    print("You can enter the exam...")
else:
    print("You can't enter the exam...")

#second - example/
attendence = 75
if_teacher_frd = True

if attendence >= 75 and if_teacher_frd:
    print("You can enter the exam...")
else:
    print("You can't enter the exam...")

#third example/
attendence = 50
if_teacher_frd = True

if not attendence >= 75:
    print("You can enter the exam...")
else:
    print("You can't enter the exam...")