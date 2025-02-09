#list/
products=["sugar","milk","bread"]
print(products)

#Adding elements\
#append/
products.append("oil")
print(products)

#insert/
products.insert(1,"nuts")
print(products)

#Changing a specific element/
products[2] = "fish"
print(products) 

#Removing elements/
#remove/
products.remove("fish")
print(products)

#pop/at pops from back side/
products.pop()
print(products)

#pop/we can pop any were form list by using indexing/
products.pop(0)
print(products)

#clear/it removes every thing from list/
products.clear()
print(products)