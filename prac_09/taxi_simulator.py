class Taxi:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.price_per_km = 1.2

    def __str__(self):
        return "{} - {:.2f} fuel units remaining".format(self.name, self.fuel)

    def drive(self, distance):
        required_fuel = distance * 10
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
            return True
        else:
            return False

    def get_fare(self, distance):
        return distance * self.price_per_km


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().get_fare(1) * fanciness  # Use get_fare method

    def __str__(self):
        return "{} - {:.2f} fuel units remaining, fanciness {}".format(self.name, self.fuel, self.fanciness)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{}. {}".format(i + 1, taxi))


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    while True:
        print("\nAvailable Taxis:")
        display_taxis(taxis)

        choice = input("Choose a taxi by entering its number (or 'q' to quit): ")

        if choice.lower() == 'q':
            break

        try:
            taxi_choice = int(choice) - 1
            selected_taxi = taxis[taxi_choice]

            if current_taxi is not None:
                distance = float(input("Enter the distance to drive: "))
                if current_taxi.drive(distance):
                    cost = current_taxi.get_fare(distance)
                    print("Trip cost: ${:.2f}".format(cost))
                else:
                    print("Not enough fuel for the trip.")
            current_taxi = selected_taxi

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid taxi number.")

if __name__ == "__main__":
    main()
