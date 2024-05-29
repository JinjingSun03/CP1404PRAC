"""import random

def get_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 90:
            return "Excellent"
        if score > 50:
            return "Passable"
        if score < 50:
            return "Bad"

def main():
    user_score = float(input("Enter your score: "))
    user_result = get_result(user_score)
    display user_result

    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    display Random score

if __name__ == "__main__":
    main()"""


import random

def get_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 90:
            return "Excellent"
        if score > 50:
            return "Passable"
        if score < 50:
            return "Bad"

def main():
    user_score = float(input("Enter your score: "))
    user_result = get_result(user_score)
    print(user_result)

    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(f"Random score ({random_score}): {random_result}")

if __name__ == "__main__":
    main()
