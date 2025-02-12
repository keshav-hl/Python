#Distributing Laddus/
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya","keshav","shiva"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")