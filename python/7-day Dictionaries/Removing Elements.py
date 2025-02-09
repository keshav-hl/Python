#pop()/
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "Ramanagara": "Ragi mude"
}
print(karnataka_food)
Mysuru_food = karnataka_food.pop("Mysuru")
print(Mysuru_food)

#or to pop/
print(karnataka_food.pop("Mangaluru"))

#del/ 
del karnataka_food["Bengaluru"]
print(karnataka_food)

#clear()/
karnataka_food.clear()
print(karnataka_food)
