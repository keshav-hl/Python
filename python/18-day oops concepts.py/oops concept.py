class car:
    def __init__(self,car_id, name, year, price_per_day, status, rented_days):
        self.car_id = car_id
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.status = status
        self.rented_days  = rented_days

    def display_details(self):
        print(f"Car ID: {self.car_id}, Name: {self.name}, Year: {self.year}, Price_per_day: {self.price_per_day}, Status: {self.status}, Rented_days: {self.rented_days}")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Car {self.car_id}, Status updated to {self.status}.")

    def calculate_rantal_price(self):
        total_price = self.price_per_day * self.rented_days
        print(f"Total price: {total_price}.")

car1 = car(1,"swift",2020,50,"Available",3)
car2 = car(2,"fortuner",2021,150,"Available",5)

car2.display_details()
car1.update_status("rented")
car2.calculate_rantal_price()