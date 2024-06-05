user_name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(user_name)

with open('name.txt', 'r') as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")

with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()[:2]]
    result = sum(numbers)
    print(f"The sum of the first two numbers is: {result}")

with open('numbers.txt', 'r') as file:
    all_numbers = [int(line.strip()) for line in file.readlines()]
    total = sum(all_numbers)
    print(f"The total of all numbers is: {total}")
