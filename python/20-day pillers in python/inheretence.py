#Example-1 Inheretence in python/
class user():
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def user_name(self):
        print(f"user name is {self.name}.")
    
    def log_in(self):
        print(f"{self.name} is loged in.")

class admin(user):
    def __init__(self, name, password):
        super().__init__(name, password)
    
    def delete_user(self):
        print(f"{self.name} is deleted.")

user1 = admin("keshav", "Keshav@2543")
user1.log_in()
print(user1.name)
user1.user_name()
user1.delete_user()
print(" ")

#Example-2 inherietence/
class family:
    def __init__(self, sirname):
        self.sirname = sirname

    def sirname(self):
        print(f"Sir name is {self.sirname}.")

class child(family):
    def __init__(self, sirname, name):
        super().__init__(sirname)
        self.name = name

    def name(self):
        print(f"Child name is {self.name}.")

child1 = child("gowda", "keshav")
print(f"{child1.name} {child1.sirname}")
print(child.name(child1))
