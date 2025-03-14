#Constructer in Python/
class boy:
    def __init__(self, name, address):  #__init__ is a constructer/
        self.name = name
        self.address = address

    def boy_detail(self):
        print(f"Boy name is {self.name} and He is from {self.address}.")

boy1 = boy("keshav", "Hullikate")
boy1.boy_detail()
