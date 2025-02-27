# Creating a list/
name = ["keshav", "dilip" , "shiva" , "pramod"]
numbers = [1,23,34,45,66]
mixed = ["keshav", 4, "shiva", 34, True]
print(mixed)
print(numbers)
print(name)

#Accessing list elements/
name = ["keshav", "shiva", "pramod", "dilip"]
print(name[1])
print(name[-1])
print(name[0])

#Modifying list elements/
#adding list elemets/
name = ["keshav", "shiva", "dilip", "pramod"]
name[1] = "vadekar"
print(name)
name.append("Ananaya")
print(name)
name.insert(2,"Priyanka")
print(name)

#Removing list elements/
name.remove("Priyanka")
print(name)
name.pop(1)
print(name)
name.pop()
print(name)
name.clear()
print(name)

#slicing the list/
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[1:5])
print(numbers[:])
print(numbers[:-4])
print(numbers[5:])
print(numbers[0::2])
print(numbers[::-1])

#list common functions/
print(len(numbers))
print(sorted(numbers))
print(sum(numbers))

#list common methods/
fruits = ["apple", "banana","mango","papaya","apple"]
print(fruits.index("mango"))
print(fruits.count("apple"))
fruits.reverse()
print(fruits)

#Nested list/
l =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(l)
print(l[0])
print(l[0][1])
