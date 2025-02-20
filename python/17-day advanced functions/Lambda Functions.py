#Lambda Functions/
x = lambda a,b: a+b
print(x(2,4))

sub = lambda a,b: a-b
print(abs(sub(2,4)))

sqr = lambda x: 2*x
print(sqr(2))

#Nested Functions/
def outer_fun(name):
    def inner_fun():
        print(f"your name is: {name}.")
    inner_fun()
outer_fun("keshav")

#example 2 nested function/
def calculater(a,b):
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
calculater(4,2)