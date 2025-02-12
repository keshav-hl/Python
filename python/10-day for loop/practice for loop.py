#Difference between for loop and while loop/
#while loop to print 1 to 10 numbers/
i = 1

while i <=10:
    print( i , end="  ")
    i += 1 
print(" ")

#for loop to print 1 to 10 numbers/
for i in range(1 ,11):
    print(i , end="  ")
print("")

#for loop example-1/
bag = ["red","blue","green"]
for balls in bag:
    print(balls)

#Example-2 splitting letters/
name = ("keshav")
for letters in name:
    print(letters*2)

#Example-3/
for i in range(1):
    print("keshav")

#Example-4/
l = ("keshav")
for index, num in enumerate(l):
    print(f"{num} is in {index} index.")

#Example-5/else and break in for loop/
l =[12,23,445,656,456,87]

for num in l:
    print(num)
    if num == 656:
        break
else:
    print("All printed..")

#Example-6/ continue in for loop/
name = ["keshav","pramod","shiva","dilip"]

for i in name:
    if i == "shiva":
        continue
    print(i)

#Example-7/ for loop in dictionary/
dic = {"name":"keshav", "age":20, "income":20}
print(dic.items())

for key , Value in dic.items():
    print(key,":", Value)

#Example-8/ nested for loop/ tables from 1 to 10.
for i in range(2,11):
    for j in range(2,11):
        print(f"{i} x {j} = {i*j}")

#Example-9/ only 2 tables.
for i in range(1,11):
    print(f"2 X {i} = {2 * i}")