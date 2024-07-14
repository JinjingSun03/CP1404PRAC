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

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar1)

current_year = 2023
print("Age:", guitar1.get_age(current_year))
print("Is Vintage:", guitar1.is_vintage(current_year))

def test_guitar_methods():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013)

    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age(2022)}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age(2022)}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(2022)}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(2022)}")

test_guitar_methods()
