#tuples in python/
tup = ("keshav", "shiva", "pramod", "dilip", "vade")
print(tup)

num = (1,2,3,4,5)
print(num)

single = ("apple", )
print(single)

#Accessing tuple elements/
print(tup[1])
print(tup[2:4])
print(tup[-1])
print(tup[1::2])
print(num[::-1])

#Concatination of tuples/
num1 = (6,7,8,9) * 3
numbers = num + num1
print(numbers)

#repetation in tuples/
print(num1)

#membership in tuples/
print("keshav" in tup)
print(5 in num)

#tuple methods/
#indexing method/
names = ("keshav", "pramod", "dilip", "shiva", "vade")
print(names.index("pramod"))
print(names.index("keshav"))

#count method/
my_tuple = (1,2,3) * 4
print(my_tuple)
print(my_tuple.count(1))
