"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

"""try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")"""

"""When will a ValueError occur?
A ValueError will occur if the user enters a value that cannot be converted to an integer when trying to convert the
input to numerator or denominator. For example, entering a non-numeric value like "abc" will trigger a ValueError.

When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator. Division by zero is undefined in mathematics,
so this error is raised to prevent such situations.

Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can change the code to include a conditional statement to check if
the denominator is zero before performing the division. If the denominator is zero, 
you can handle it separately.
"""

"""try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        display ("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        display (fraction)

except ValueError:
    display ("Numerator and denominator must be valid numbers!")

display ("Finished.")
"""

while True:
    try:
        numerator = int(input("Enter the numerator (or type 'q' to quit): "))
        if numerator == 'q':
            break

        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

print("Finished.")
