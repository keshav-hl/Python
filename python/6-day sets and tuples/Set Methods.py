#sets/
fruits = {"apple","banana","cherry"}
print(fruits)

#add()/
fruits.add("orange")
print(fruits)

#remove()/ it will show error if the given element is not in the set/
fruits.remove("orange")
print(fruits)

#discard()/ it will not show any error if the given element not in the set/
fruits.discard("orange")
print(fruits)

#pop()/ it removes random element in the set/
fruits.pop()
print(fruits)

#clear()/ it will remove everything in the set/
fruits.clear()
print(fruits)