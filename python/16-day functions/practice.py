#first-Example functions/
def greed():
    print("boy marraies a girl.")

greed()
greed()
print(" ")

#second example/
def marrage(boy, girl):
    print(f"boy name {boy}")
    print(f"girl name {girl}")
    print(f"{boy} marries a {girl}.")

marrage("keshav", "kesh")
print(" ")
marrage("hsdgh","jdhs;kad")

#third Example tables in functions/
#common tables/
for i in range(1,11):
    print(f"2 X {i} = {2*i}.")
print(" ")

for i in range(1,11):
    print(f"3 X {i} = {3*i}.")
print(" ")

#tables with functions/
def tables(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}.")
tables(2)
print(" ")
tables(3)
print(" ")
tables(8)

#fourth example none values/
def marrage(boy, girl="gotilla"):
    print(f"boy name {boy}")
    print(f"girl name {girl}")
    print(f"{boy} marries a girl {girl}.")

marrage("keshav")

#fifth example return values/
def num(num):
    return (int(str(num)*5))

a = 1000
b = num(2)
c = a + b
print(c)

#sixth example local and global variables/
def loc():
    x = "keshav" #local variables/
    print("My name is keshav.")
loc()

y = "kesh" #global variables/
print(y)
