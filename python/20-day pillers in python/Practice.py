#Abstraction in python/
l = [1,2,3]
print(l)
l.append(4) #Inserting the element to the list/
print(l)

#Real abstraction code/
class car:
    def car_start(car):
        print("Car started..")
    def car_stop(car):
        print("Car stoped..")
    def car_go_fast(car):
        print("Press the Accelerator..")
car1 = car()
car1.car_go_fast()
car1.car_stop()
car1.car_start()
print(" ")

#Encapsution in python/
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(f"your balance {self.__balance}")

    def add_money(self, add_money):
        self.__balance += add_money
        print(f"Added money: {add_money}. New Balance: {self.__balance}.")

    def withdraw_money(self, withdraw_money):
        self.__balance -= withdraw_money
        print(f"WithDraw money: {withdraw_money}. New Balance: {self.__balance}.")

rbi = ATM(1000)
rbi.show_balance()
rbi.add_money(500)
rbi.withdraw_money(200)
rbi.show_balance()

#Example-2 Encapsulation/
class user_login:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def user_name(self):
        return self.username

    def check_password(self, new_password):
        return new_password == self.__password

user1 = user_login("keshav", "Keshav@2543")

print(user1.username)
user1.user_name()
print(user1.check_password("23456789iujhgf"))
print(user1.check_password("Keshav@2543"))

#Example to both Abstraction and Encapsulation/
class database:
    def __init__(self):
        self.__storage = { }

    def store_data(self, key, values):
        self.__storage[key] = values
        print(f"Data saved for: {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")

database1 = database()
database1.store_data("01",{"name" : "keshav", "age" : 20})
database1.store_data("02",{"name" : "Pramod", "age" : 21})
print(database1.get_data("01"))
print(database1.get_data("02"))
print(database1.get_data("00"))

#Inheritance in python
# Example-1 Inheretence in python/
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


# Example-2 inherietence/
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

#Example-1 Polymorphism in python/
class animals:
    def make_sound(self):
        print("Animals make sound..")

class dog(animals):
    def make_sound(self):
        print("Bark")

class cat(animals):
    def make_sound(self):
        print("mew mew")

sounds = [animals(), dog(), cat()]
for animal in sounds:
    animal.make_sound()
print(" ")

#Example-2 Polymorphism/
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()