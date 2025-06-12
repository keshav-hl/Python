print("keshav") #output string/

name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
print(age)

#some examples/
boy_name = input("Enter boy name: ")
boy_age = int(input("Enter boy age: "))
girl_name = input("Enter girl name: ")
girl_age = int(input("Enter girl age: "))

age_diff = abs(boy_age - girl_age)

print(f"{boy_name} loves {girl_name}. Age difference is {age_diff}")
print(boy_name + " loves " + girl_name+"." + " Age difference is " + str(age_diff))
