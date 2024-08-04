# taxi.py

class Taxi:
    price_per_km = 1.23

    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.total_km = 0
        self.total_fare = 0

    def drive(self, distance):
        if self.fuel >= distance:
            self.total_km += distance
            self.total_fare += distance * self.price_per_km
            self.fuel -= distance
            return True
        else:
            print("Not enough fuel to drive that far.")
            return False

    def restart_meter(self):
        self.total_km = 0
        self.total_fare = 0

    def get_details(self):
        return f"Taxi: {self.name}, Fuel: {self.fuel} units, Price per km: ${self.price_per_km}"

    def get_fare(self):
        return f"Current Fare: ${self.total_fare}"
