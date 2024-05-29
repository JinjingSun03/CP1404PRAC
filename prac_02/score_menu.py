"""def get_valid_score():
    while True:
        try:
            get score
            if 0 <= score <= 100:
                return score
            else:
                display ("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            display ("Invalid input. Please enter a valid integer.")

def print_result(score):
    display (f"The result for the score {score} is: PASS" if score >= 50 else "FAIL")

def show_stars(score):
    display ("*" * score)

def main():
    get score

    while True:
        display Menu
        display Get a valid score
        display Print result
        display Show stars
        display Quit

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            display Farewell
            break
        else:
            display ("Invalid choice. Please enter G, P, S, or Q.")

if __name__ == "__main__":
    main()"""


def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_result(score):
    print(f"The result for the score {score} is: PASS" if score >= 50 else "FAIL")

def show_stars(score):
    print("*" * score)

def main():
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please enter G, P, S, or Q.")

if __name__ == "__main__":
    main()