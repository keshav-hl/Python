#first example key arguments/
def num(*a):
    print(a)
num(1,2,3,4,5)

#or/
def de(a , b):
    print(a+b)
de(1, 2)

#second example adding more than one number/
def num(*a):
    print(sum(a))
num(1,2,3,4,5)

#third example whitout using key arguments/
def student(name,age):
    print(f"student name: {name}")
    print(f"student age: {age}")
    print(f"{name} - {age}.")

student("keshav" , 20)
student("dilip" , 21)
student(name="pramod", age="22")

#fourth example with **kwargs/
def double(**details):
    print(details)
    for key, values in details.items():
        print(f"{key} - {values}")
double(name="keshav", age=20, cource="python")
double(name="pramod", age=21, cource="java")

#fifth examle with Lambda Functions/
#first use case/
x = lambda a,b : a+b
print(x(1,2))

double = lambda x : 2*x
print(double(200))

k = lambda a,b: a//b
print(k(8,2))

#dictionary use case/
student = [
    {"name" : "keshav", "age": 20},
    {"name" : "pramod", "age": 25},
    {"name" : "shiva", "age": 14}
]

student.sort(key= lambda x: x["age"], reverse=True)
print(student)

#recurcive functions/
#factorial program/
def keshav(n):
    if n == 1:
        return 1
    return n * keshav(n-1)
n = int(input("Enter the factorial number: "))
print(keshav(n))

#nested functions/
def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
    mul()
    div()
print(calculate(2,4))
