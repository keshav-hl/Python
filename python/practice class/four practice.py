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
