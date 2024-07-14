class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

def main():
    print("My guitars!")

    guitars = []
    guitar_number = 1

    while True:
        name = input("Name: ")
        if not name:
            break

        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.\n")

    print("\nThese are my guitars:")

    current_year = 2023

    for i, guitar in enumerate(guitars, start=1):
        vintage_status = " (vintage)" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {i}:\t{guitar.name} ({guitar.year}), worth $ {guitar.cost:.2f}{vintage_status}")

if __name__ == "__main__":
    main()
