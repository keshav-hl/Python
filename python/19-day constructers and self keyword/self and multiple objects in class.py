#Self key word in python/
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f"Person name is {self.name} and his age is {self.age}.")
    
person1 = person("keshav", 20)

person1.person_info()
print("")

#Multiple Objects with Different Attributes/
class laptop:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage

    def laptop_detail(self):
        print(f"laptop name {self.name} and it's brand name {self.storage}.")
    
laptop1 = laptop("dell", "1TB")
laptop2 = laptop("HP", "500 GB")

laptop.laptop_detail(laptop1)
laptop1.laptop_detail()
laptop2.laptop_detail()
