#Function that adds two numbers and returns the result/
def add(a, b):
    print(a+b)
add(2,3) #Here, print() simply displays the message but does not return anything

#same example using return/
def num(a, b):
    return a + b
result = num(4,2)
print(result)  #Here, return gives back the sum of a and b, which we can store and use later.

#Function with a default parameter/
def greed(name="friend"):
    print(f"hi {name}!. welocome to my Home.")
greed()
greed("pramod")
