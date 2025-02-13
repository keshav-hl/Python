#sum of numbers in for loop/
l =[12,14,3,45,56,67]
total = 0

for num in l:
    print(total)
    total += num

print(total)

#double the list and append to dl/
l =[12,14,3,45,56,67]
dl = []

for num in l:
    print(num)
    dl.append(num*2)
    print(dl)

#Dictionaries in for loop/
students_marks = {"keshav":85,"dilip":75,"pramod":80,"shiva":82}

for student, marks in students_marks.items():
    print(f"{student} - {marks}..")

#for Loops with range()/
student = ["keshav","shiva","dilip","pramod"]
marks = [24, 54, 67, 45]

students_marks = {}

for i in range(0, len(student), 2):
    students_marks[student[i]] = marks[i]

print(students_marks)

#List Comprehension/Example-1/
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

dl = [x*2 for x in l]
print(dl)

#list coprehension/ Example-2/
l = [x for x in range(1,11)]
print(l)

edl = [x for x in l if x%2==0]
print(edl)

#list coprehension/ for list names accessing letters/ Example-3/
l = ["keshav","dilip","pramod","shiva"]
print(l)

ll = [x[1] for x in l]
print(ll)

#length of strings in list coprehension/
li = ["keshav","dilip","shiva","pramod"]
print(li)

lli = {name:len(name) for name in li}
print(lli)

#Dictionary Comprehension/
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num for num in numbers}
print(squares_dict)

#Dictionary Comprehension/Example-1
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

#strings splitting/Example-1/
stri = "my name is keshav"
s = stri.split()
print(s)

#Example-2/
stri = "my-name-is-keshav"
s = stri.split("-")
print(s)

#list in put/ Example-1/
l = input("Enter the list: ").split()

ll = [int(num) for num in l]
print(ll)

#Example-2/ same as the above but different way/

ll = [int(num) for num in input("Enter the list: ").split()]
print(ll)