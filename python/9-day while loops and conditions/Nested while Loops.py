#Nested while Loops in python/
snakes = 3
money = 10

while snakes > 0 and money > 0:
    print(f"There are {snakes} snakes.")
    print(f"There are {money} money.")
    Buying = input("If you buy say(yes or no): ")

    if Buying == "yes":
        snakes -= 1
        money -= 5
        print(f"Remaining snakes:{snakes} and {money}..")
    else:
        print("May be later.")
        break
print("Either no money are no snakes..")