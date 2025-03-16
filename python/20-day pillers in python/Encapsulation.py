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
