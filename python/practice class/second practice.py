#concatenation and formated strings in python/
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("hi "+ name + "!. your age is "+ str(age))
print(f"hi {name}!. Your age is {age}")

#repeation in python/
k = "keshav " * 5
print(k)

ke = "keshav "
print(ke *6)

#String methods/
method = "hello world! "
print(method.upper())
print(method.lower())
print(method.index("w"))
print(method.split())
print(method.strip())
print(method.replace("world", "python"))
print(len(method))

#accessing string character/
ass = "pyhton!"
print(ass[5])
print(ass[0:])
print(ass[:-1])

#slicing of strings/
print(ass[::-1])
print(ass[::])
print(ass[3:6])
print(ass[0::2])

#Excape sequence/
print("My name is keshav. \n Iam 20 years old.")
print("My name is keshav. \t Iam 20 years old.")
print("My name is keshav. \\ Iam 20 years old.")
print("""My name is keshav.
                Iam 20 years old.""")

#Example - 1/
boy_name = input("Enter your name: ")
boy_age = int(input("Enter your age: "))
girl_name = input("Enter your name: ")
girl_age = int(input("Enter your age: "))

age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + ". Age difference is "+ str(age_diff) + ".")
print(f"{boy_name} loves {girl_name}. Age difference is {age_diff}.")

#Example - 2/
name = "my name is keshav!"
len_space = len(name.replace(" ",""))
print(len_space)