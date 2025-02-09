age = int(input("Age: "))
print(age)

name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
print(name, age)

boy_name = input("Enter your name: ")
boy_age = int(input("Enter your age: "))
girl_name = input("Enter your name: ")
girl_age = int(input("Enter your age: "))

age_diff = abs(boy_age - girl_age)

print(boy_name  +" loves "+  girl_name + ". Age difference is " + str(age_diff))
print(f"{boy_name} loves {girl_name} . age difference is {age_diff}")


