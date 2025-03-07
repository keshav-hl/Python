#variable length arguments/
def arg(*a):
    return sum(a)
print(arg(10,23,20))

#Example - 2/
def de(a,b):
    return a + b
print(de(10,20))

#Example - 3/
def all(*number):
    return sum(number)
print(all(10,20,39))

#key world arguments in functions/
def count(**details):
    print(type(details))
    print(details)
    for key, values in details.items():
        print(f"{key} : {values}")
count(name="keshav", age=20, gender="Male")

#Lamda functions/
add = lambda a,b: a + b
print(add(24,24))

double = lambda a: 2*a
print(double(500))

#advanced lambda functions/
student = [
    {"name" : "keshav", "marks" : 10},
    {"name" : "pramod", "marks" : 100},
    {"name" : "shiva", "marks" : 50},
    {"name" : "Dilip", "marks" : 30}
]

student.sort(key= lambda x: x["marks"], reverse=True)
print(student)

#Example - 2  factorial/
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter the factorial number: "))
print(factorial(n))

#nesteb function/
def calculater(a, b):
    def add():
        print(a + b)
    def sub():
        print(a - b)
    def mul():
        print(a * b)
    def div():
        print(a / b)
    add()
    sub()
    mul()
    div()
calculater(2,5)
