#day-3 home work greeting program/
name = input("Enter your name: ")
pre = 15
now = 5

print(f"Hey {name}! 😊 we are meeting after {now} years.your age is {pre} then.know I think it's {pre+now}.Hope you're having an amazing day! Remember, you're awesome, and I'm always here if you need anything. Take care! 💙✨")

# input from the user and upper case and lower case to the input/
s = input("Enter the name: ")

print(s.upper())
print(s.lower())
print(s.replace(" ","_"))
print(s.strip())

#input a string by user and count the string Excluding spalce/ 
print(len(s.replace(" ", "")))

#proble Example/
print("""Hello
    World""")
print("This is a backslash: \\")