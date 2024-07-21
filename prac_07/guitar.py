"""class Guitar:
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
"""

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

guitars = []

with open("prac/guitars.txt", "r") as file:
    for line in file:
        name, year, cost = line.strip().split(',')
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

print("Guitars:")
for guitar in guitars:
    print(f"{guitar.name}, {guitar.year}, ${guitar.cost:.2f}")

guitars.sort()

print("\nSorted Guitars (by year):")
for guitar in guitars:
    print(f"{guitar.name}, {guitar.year}, ${guitar.cost:.2f}")

"""git add your_script.py
git commit -m "Complete first part of More Guitars exercise"
"""
