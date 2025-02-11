#user input/Example-1/
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative numbers..")
    age = int(input("Enter your age: "))
else:
    print(f"you age is {age}.. you are too young.")


#Example-2/
name =input("Enter your name: ")

while name =="":
    print("you cant leave it empty..")
    name = input("Enter your name: ")
else:
    print(f"Hi {name}. good morning..")

#Example-3/
food = input("Enter a food you like (press 'q' to stop): ")

while not food == "q":
    print(f"Your liked food is {food}.")
    food = input("Enter another food you like (press 'q' to stop): ")

print("bye")

#Example-4
num = int(input("Enter numbers between 1 to 10: "))

while num < 1 or num > 10:
    print(f" The {num} is not valid..")
    num = int(input("Enter numbers between 1 to 10: "))
else:
    print("The {num} is valid..")

#Example-5/
pin = " "
correct_pin = "1234"

while pin != correct_pin:
    pin = (input("Enter the pin: "))
    if pin != correct_pin:
        print(f"Entered {pin} is incorrect..")
else:
    print("Entered pin correct")
print("wlecome!")
