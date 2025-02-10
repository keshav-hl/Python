#Checking Bus Ticket Prices/
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))

if gender == "female":
    print("Ticket is free!")
elif age < 5:
    print("Ticket is free!")
elif age >= 50:
    print("You get above age dis-count")
else:
    print("You should pay full ticket..")
