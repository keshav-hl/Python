#functions in python/
#difference/
print("Hello Good Morning!")
print("Hello Good Morning!")
print("Hello Good Morning!")
print("")

#This can be use in functions/
def kesh():
    print("Hello good Morning!")
kesh()
kesh()
kesh()

#Example second/
def student(boy):
    print(f"Boy is {boy}.")
student("keshav")
student("pramod")
student("shiva")
student("dilip")

#Example Third/
#Strings Example/
boy_name = input("Enter boy name: ")
boy_age = int(input("Enter boy age: "))
girl_name = input("Enter girl name: ")
girl_age = int(input("Enter girl age: "))

age_diff = abs(boy_age - girl_age)

if boy_age > girl_age:
    print(f"boy is {age_diff} years greater than girl.")
elif boy_age < girl_age:
    print(f"girl is {age_diff} years greater than the boy.")

print(f"{boy_name} loves {girl_name}.")

#same Example in functions/
def name(boy_name, girl_name):
    def age(boy_age, girl_age):
        print(f"boy age is {boy_age}")
        print(f"girl age is {girl_age}")
        age_diff = abs(boy_age - girl_age)

        if boy_age > girl_age:
            print(f"boy is {age_diff} years greater than girl.")
        elif boy_age < girl_age:
            print(f"girl is {age_diff} years greater than the boy.")
    age(20, 22)
    print(f"boy is {boy_name}")
    print(f"girl is {girl_name}")
    print(f"{boy_name} loves {girl_name}")
name("keshav", "kesh")

#positional arguments/
def greet(name, location):
    print(f"Hello {name}")
    print(f"Your location is {location}")
greet("keshav","Magadi") #Positional arguments/
print(" ")
greet(location="Magadi", name="Keshav") #Keyworld arguments/

#Tables function/
def tables(num):
    for i in range(1,11):
        print(f"{num} X i = {num*i}")
tables(5)
tables(6)

#defalt parameter/
def marrage(boy, girl="don't now"):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
marrage("keshav")

#Return function/
def func(num):
    return int(str(num)*2)

b = func(2)
a = 20

c = a + b
print(c)

#local variables/
def var():
    x = "keshav" #local variable which can only call inside the function/
    print("Hello Keshav!")
    print(x)
    print(y)

y = "pramod" # global variable/
print(y)