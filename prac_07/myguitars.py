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