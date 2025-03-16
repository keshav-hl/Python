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