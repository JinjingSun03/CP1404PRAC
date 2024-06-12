import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = 5
NUMBERS_PER_QUICK_PICK = 6

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK))

def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))

if __name__ == "__main__":
    main()
