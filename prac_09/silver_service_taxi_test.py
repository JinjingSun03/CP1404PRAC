from silver_service_taxi import SilverServiceTaxi


def main():
    hummer_taxi = SilverServiceTaxi("Hummer", 200, fanciness=4)
    distance = 18
    fare = hummer_taxi.calculate_fare(distance)

    print(f"{hummer_taxi}\nFare for a {distance} km trip: ${fare:.2f}")


if __name__ == "__main__":
    main()
