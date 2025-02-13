#Squaring numbers in a list/
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

# Filtering even numbers/
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

#Uppercasing Kannada city names/
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercased_cities = [city.upper() for city in cities]
print(uppercased_cities)