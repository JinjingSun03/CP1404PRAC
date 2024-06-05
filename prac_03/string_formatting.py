"""get name
get year
get cost

display (f"{year} {name} for about ${cost:,.0f}!")

for i in range(0, 201, 50):
    display (f"{i:>3}")"""


name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print(f"{year} {name} for about ${cost:,.0f}!")

for i in range(0, 201, 50):
    print(f"{i:>3}")
