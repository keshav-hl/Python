cars = {
    1 : {"name" : "swift", "year" : 2019, "status" : "Available", "price_per_day" : 50, "ranted_days" : 0},
    2 : {"name" : "Toyota", "year" : 2020, "status" : "rented", "price_per_day" : 60, "ranted_days" : 3},
    3 : {"name" : "Mustang", "year" : 2021, "status" : "available", "price_per_day" : 80, "ranted_days" : 0}
}

def display_car_details(car_id):
    car = cars.get(car_id)
    if car:
        print(f"Caar_id : {car_id}, Name: {car["name"]}, Year: {car["year"]}, Status: {car["status"]} ")
    else:
        print("not found")

def update_car_status(car_id, new_status):
    if car_id in cars:
        cars[car_id]["status"] = new_status
        print(f"Car {car_id} status updated to {new_status}.")
    else:
        print("Car not found")

def calculate_rant(car_id):
    car = cars.get(car_id)
    if car:
        total_rant = car["price_per_day"] * car["ranted_days"]
        print(f"Total rent: {total_rant}.")

update_car_status(1,"ranted")
display_car_details(1)
display_car_details(2)
calculate_rant(2)
