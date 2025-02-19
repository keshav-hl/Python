#first home work problem/
foods = ["idli", "vada", "puri","saysa","mude"]
upp_food = [food.upper() for food in foods]
print(upp_food)

#second home work problem/
d = {
    "ragi" : 50,
    "weet" : 40,
    "batagi" : 86,
    "rice" : 55
}
total = 0
for values in d.values():
    total += values
print(total)

print(sum(list(d.values())))

#third home work problem/
li = [num*2 for num in range(1,11)]
print(li)

#fourth howe work problem/
l = [
    {
        "name" :"kehsav",
        "age" : 20,
        "marks" : 50
    },
    {
        "name" : "pramod",
        "age" : 20,
        "marks" : 70
    },
    {
        "name" : "shiva",
        "age" : 21,
        "marks" : 24
    }
]
for i in l:
    print(i["name"], "-", i["marks"])

#fifth hpme work problem/
row = int(input("Enter the row element: "))
column = int(input("Enter the column element: "))

matrix = []

for i in range(row):
    row = []
    for j in range(column):
        x = int(input("Enter the element: "))
        row.append(x)
    matrix.append(row)

print(matrix)
