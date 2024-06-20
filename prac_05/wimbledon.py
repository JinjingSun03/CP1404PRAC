def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)
    return data

def count_wimbledon_wins(data):
    wins_count = {}
    for row in data:
        player = row[0]
        wins = int(row[1])
        if player in wins_count:
            wins_count[player] += wins
        else:
            wins_count[player] = wins
    return wins_count

def get_countries(data):
    countries_set = set()
    for row in data:
        countries_set.add(row[2])
    return sorted(list(countries_set))

def display_champions(wins_count):
    print("Wimbledon Champions:")
    for player, wins in wins_count.items():
        print(f"{player} {wins}")

def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    wins_count = count_wimbledon_wins(data)
    countries = get_countries(data)

    display_champions(wins_count)
    display_countries(countries)

if __name__ == "__main__":
    main()
