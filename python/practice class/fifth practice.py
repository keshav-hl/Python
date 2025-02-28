#Dictionary elements/
karnataka_foods = {
    "bangaluru" : "bisi bele bath",
    "mysure" : "mysure pak",
    "bidar" : "Rotti",
    "mangluru" : "nir dosa"
}
print(karnataka_foods)

#Accessing dictionary elements/
print(karnataka_foods.get("mysure"))
print(karnataka_foods.get("ramanagara", "ella ali adu"))

#Adding and updating dictionary elements/
#adding and updating are same/
karnataka_foods["ramanagara"] = "ragi mude"
print(karnataka_foods)

#Removing dictionary items/
karnataka_foods.pop("bidar")
print(karnataka_foods)

del karnataka_foods["mangluru"]
print(karnataka_foods)

'''karnataka_foods.clear()
print(karnataka_foods)
'''
#Dictionary methods/
#keys/
print(karnataka_foods.keys())

#values/
print(karnataka_foods.values())

#items/
print(karnataka_foods.items())

#update with new dictionary/
new_dict = {"mangluru" : "nir dose"}
karnataka_foods.update(new_dict)
print(karnataka_foods)
