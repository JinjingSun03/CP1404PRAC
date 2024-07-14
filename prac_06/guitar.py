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

