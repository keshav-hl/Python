#for loop practice/
balls = ["red","green","yellow"]
for bags in balls:
    print(bags)

#Example-2/
num = [11,22,33,44,55,66,77,88,99]
for i in num:
    print(i)

#Example-3/
for num in range(1,10,2):
    print(num)

#Example-4/
name = "keshav"
for i,name in enumerate(name):
    print(name*(i+1))

#break/
num = [1,2,3,4,5]
for i in num:
    print(i)
    if i == 3:
        break

#continue/
for i in num:
    if i == 3:
        continue
    print(i)

#Example-5/
for i in num:
    print(i)
    if i == 4:
        break
else:
    print("all printed.")

#dictionaries in for loop/
my_self = {"name":"keshav","age":"20","garaduation":"Engineering"}

for keys, values in my_self.items():
    print(f"{keys} : {values}..")

#Tables for loop/
for i in range(1,11):
    print(f"2 x {i} = {2*i}")

#Nested for loop/
for i in range(2,11):
    print("\n")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}", end="  ")

#sum of list numbers in for loop/
l = [11,22,34,45,56,67]
total = 0
for num in l:
    total += num
    print(total)

#Double and adding the list elements to other list/
l = [11,22,34,45,56,67]
dl = []
for i in l:
    dl.append(i*2)
    print(dl)

#two list elements to dictionary/
name = ["keshav","pramod","shiva","dilip"]
marks = [23,45,56,75]
students_marks = {}

for index,student in enumerate(name):
    students_marks[student] = marks[index]
print(students_marks)

#Another way/
name = ["keshav","pramod","shiva","dilip"]
marks = [23,45,56,75]

students_marks = {}

for i in range(1,len(name),2):
    students_marks[name[i]] = marks[i]
print(students_marks)

#list Comprehension/
l = [1,2,3,4,5,6,7,8,9]
print(l)

dl = [x*2 for x in l]
print(dl)

#or another Example
l = [x for x in range(1,11)]
print(l)

dl = [x*2 for x in l if x%2!=0]
print(dl)

#dictionary comprehension/
name = ["keshav","pramod","shiva","dilip"]
marks = [23,45,56,75]

student_marks ={n:len(marks) for n in name}
print(student_marks)

#Example-2/
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
cp = {key:value for key,value in city_population.items() if value>10}
print(cp)

#spliting strings/
l = "my name is keshav"
print(l.split())

#list in put/
name = input("Enter your name: ").split()
x = [int(na) for na in name]
print(x)