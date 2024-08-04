from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40)

print(my_taxi.get_details())
print(my_taxi.get_fare())

my_taxi.restart_meter()
my_taxi.drive(100)

print(my_taxi.get_details())
print(my_taxi.get_fare())

