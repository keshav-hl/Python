#for looping/
bag = ["reb","green","blue","yellow"]
for ball in bag:
    print(ball)

#Example 2 in for looping/
cities = ["bangluru","ramanagara","kanakpura","magadi","kunigal"]
for citi in cities:
    print(citi)

#Range in for looping/
for i in range(1, 11):
    print("Numbers: " + str(i))

#Range Example 2/
for i in range(2, 11, 2):
    print(f"Even numbers: {i}")

#Even numbers in while loop/
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(f"Even numbers: {i}")
    i += 1
print("Even numbers are printed...")

#same but another example/
even = True
i = 1
while even:
    if i % 2 != 0:
        i += 1
        continue
    print(f"Even: {i}")
    i += 1
    if i > 10:
        break
print("Even numbers...")

#Example of while loop/
i = 0
while i <= 10:
    x = 0
    while x < i:
        print("*", end=" ")
        x += 1
    print("")
    i += 1

#looping over strings/
l = ["keshav","dilip","pramod","shiva"]
for i in l:
    print(f"{i[0]} - {i}")
print("")

#example - 2/
name = "keshav"
for i in name:
    print(i)

#Enumerate in for loop/
name = "keshav"
for index, letter in enumerate(name):
    print(f"{index} - {letter}")

#Enumerate over list of items/
l = [12,23,34,45,55,56,66,76,78,90]
for index, num in enumerate(l):
    print(f"{index} - {num}")

#Continue in for loop/
cities = ["bangluru","mysure","mangluru","magadi"]
for city in cities:
    if city == "mangluru":
        continue
    print(city)
print("")

#Break in for loop/
names = ["keshav","pramod","shiva","dilip","Nandish"]
for name in names:
    if name == "Nandish":
        break
    print(name)

#else in for loop/
numbers = [12,11,23,33,43,54,55,66,87]
for num in numbers:
    if num == 55:
        break
    print(num)
else:
    print("All are printed..")

#dictionaries in for loop/
d = {"name" : "keshav", "age": "20", "collage" : "dayananda sagar"}

for key, values in d.items():
    print(f"{key} - {values}")

#Nested loop in for looping/
for i in range(1, 11):
    print(f"2 X {i} = {2*i}")

#second Example in nested loop/
for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")

