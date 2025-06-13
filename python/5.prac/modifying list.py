#list/
fruits = ["apple", "banana", "orange"]
print(fruits)

#adding elements into list/ 
fruits[1] = "mango" #It will replace the element/
print(fruits)

#anther method/
fruits.append("cherry")  #It will add the element to list/
print(fruits)

#third example/
fruits.insert(1, "banana")  #It will add elment to the specfic element/
print(fruits)

#Removes the element from the list/
fruits.remove("cherry")  #it removes the given element/
print(fruits)

#second example/
fruits.pop()  #it removes the last element/ 
print(fruits)

#element removeing by indexing/
fruits.pop(0)
print(fruits)