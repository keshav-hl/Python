#enumerate in for loop/
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")
print(" ")


#else in for loop/
for city in cities:
    print(city)
else:
    print("No more cities!")