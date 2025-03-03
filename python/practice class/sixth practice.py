#While looping/
condition = True

while condition:
    print("condition is true.")

#Second Example while loop/
condition = True
i = 1
while condition and i<=100:
    print(f"try {i}.")
    i += 1
print("\tGive UP..")

#Third Example/
if_true = True
i = 1
while if_true:
    if i % 2 != 0:
        i += 1
        continue
    print(f"Try {i}.")
    i += 1
    if i > 100:
        break
print("\t Give UP...")

#fourth Example/
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
print("Even numbers are printed...")

#Fifth Example/
i = 0
while i <= 10:
    x = 0
    while x < i:
        print("keshav", end=" ")
        x += 1
    print("")
    i += 1

#Password generater/
pin = 1234
input_pin = True
trial = 1
while trial <= 3:
    input_pin = int(input(f"Trial-{trial} | Enter the pin: "))
    trial += 1
    if input_pin == pin:
        print("correct pin.")
        break
    else:
        print("incorrect pin.")

#Real life Example/
snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()

    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        break

print("Either snacks are sold out or you are out of money.")
