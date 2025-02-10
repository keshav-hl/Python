#first example/-----
num = int(input("Enter the number: "))

if num % 2 == 0:
    print("Number is even..")
else :
    print("Number is odd..")
    
#second example/-----
signal = input("Enter the signal: ")

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
elif signal == "green":
    print("GO")
else :
    print("NO SIGNAL...")

#third example/Comparison Operators in if Statements/-----
age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote!")
else:
    print("you can't vote!")