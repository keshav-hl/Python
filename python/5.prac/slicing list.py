#Slicing in python/
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[1::2])
print(numbers[1:])
print(numbers[::-1])
print(numbers[2:6])

#list functions and methods/
#common functions/
print(len(numbers))
print(sum(numbers))
num = [2,3,1,4,7,5]
print(sorted(num))

#common methods/
fruits = ["apple", "banana", "mango", "cherry"]
print(fruits.index("apple"))

#it will count the numbers/
num = [1,2,3,1,3,1,5]
print(num.count(1))
fruits.append("papaya")
print(fruits)

#it will sort the numbers/
num.sort()
print(num)

#reverse the numbers/
num.reverse()
print(num)

#example-2 reverse/
fruits.reverse()
print(fruits)

#nested list/
m = [[1,2], [3,4]]
print(m)
print(m[0])
print(m[1])
print(m[0][1])
print(m[1][0])