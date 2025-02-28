#Tuples in python/
fruits = ("apple","banana","cherry","papaya","mango")
print(fruits)
numbers = (1,2,3,4,5,6)
print(numbers)

#Single element in the list/
fruit = ("apple",)
print(fruit)

#Accessing tuple elements/
print(fruits[4])
print(fruits[:5])
print(fruits[::-1])
print(fruits[1::2])

from tkinter.font import names

#Tuple operations/
#Tuple Concatenation/
num1 = (1,2,3,4,5)
num2 = (6,7,8,9,10)
num = num1 + num2
print(num)

#tuple repetation/
names = ("keshav", "pramod") *3
print(names)

#Checking Membership/
print("shiva" in names)

#Tuple Methods/
#count method/
number = (1,2,3,4,4,2,5,1,2,1,1)
print(number.count(1))

#Indexing method/
print(number.index(4))

#Sets in python/
#Creating sets/
fruits_sets = {"apple","orange","banana","cherry","mongo"}
numbers_sets = {1,2,3,4,5,6,7,8,9}
print(fruits_sets)
print(numbers_sets)

#empty sets/
empty_set = set()
print(empty_set)

#set operations/
set1 = {1,2,3}
set2 = {3,4,5}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

diff = set1 - set2
print(diff)

sem_diff = set1 ^ set2
print(sem_diff)
''
#set methods/
sets = {"apple", "banana","cherrry"}

#add method/
print(sets.add("mango"))
print(sets)

#remove method/
sets.remove("banana")
print(sets)

#discard method/
sets.discard("water mellan")
print(sets)

#pop method/
print(sets.pop())

#clear method/
sets.clear()
print(sets)
