#Keyword Arguments in python/
def word(name, age):
    print(f"{name} - {age}.")
word("keshav",20)
word("pramod",30)

#*args arguments in python/
def student(*a):
    print(sum(a))
student(1,2,3,4,5)

#**kwargs in python/
def stud(**details):
    print(details)
    for key, values in details.items():
        print(f"{key} - {values}.")
stud(name="keshav", age=20, cource="python")
stud(name="shiva", age=22, cource="projects")
