import random

class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def drive(self, distance):
        if self.fuel >= distance:
            self.fuel -= distance
            return distance
        else:
            driven_distance = self.fuel
            self.fuel = 0
            return driven_distance

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            driven_distance = super().drive(distance)
            print(f"{self.name} drove {driven_distance} km.")
            return driven_distance
        else:
            print(f"{self.name} failed to drive due to low reliability.")
            return 0

# Example usage:
car1 = UnreliableCar("UnreliableCar1", 50, 70)
distance_driven = car1.drive(30)
print(f"Total distance driven: {distance_driven} km")
