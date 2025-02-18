#first home work problem/
i = 0

while i <= 10:
    print(i)
    i += 1

#second home work problem/
i = 0

while i <= 20:
    i += 1
    if i % 2 != 0:
        print(i)

#third home work problem/
seats = 8
while seats > 0:
    x = input("book a seat(yes/no): ")
    if x == "yes":
        seats -= 1 
        print("Remaining seats are", seats)
    else:
        print("tq for visiting out sight!")
        break
else:
    print("all seats are booked.")

#fourth home work problem/
import time
i = 11

while i>0:
    i -= 1
    time.sleep(1)
    print(i)
    