#KSRTC bus seat booking system/
aval_seats = 5

while aval_seats > 0:
    print(f"{aval_seats} seats are available..")
    booking = input("you want to book a seat (yes (or) no): ")

    if booking == "yes":
        aval_seats -= 1
        print(f"{aval_seats} remained seats..")
        print("thank-you.")
    else:
        print("no bookings are made..")
        print("May be later.")

