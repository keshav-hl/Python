#procigular code in python/
cars = {
    1 : {"name" : "swift", "year" : 2021, "price_per_day" : 50, "ranted_days" : 2},
    2 : {"name" : "Totata", "year" : 2022, "price_per_day" : 100, "ranted_days" : 4},
    3: {"name" : "fortuner", "year" : 2024, "price_per_day" : 150, "ranted_days" : 6}
}

def car_details(car_id):
    car = cars.get(car_id)
    if car:
        print(f"Car Name: {car["name"]}, Year: {car["year"]}, Price_per_day: {car["price_per_day"]}, Ranted days: {car["ranted_days"]}")
    else:
        print("car not found")

car_details(2)

def update_year(car_id, new_year):
    car = cars.get(car_id)
    if car:
        print(f"Old year: {cars[car_id]["year"]}")
        cars[car_id]["year"] = new_year
        print(f"updated year: {new_year}")
    else:
        print("car not found")

update_year(2,"2023")
car_details(1)
car_details(2)
car_details(3)

def total_rante_of_cars(car_id):
    car = cars.get(car_id)
    if car:
        total_rant = car["price_per_day"] * car["ranted_days"]
        print(f"Total rant of a car: {total_rant}.")
    else:
        print("car not found")

total_rante_of_cars(3)
total_rante_of_cars(1)
total_rante_of_cars(2)

