import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""Line 1:
This prints a random integer between 5 and 20 (inclusive).
The smallest number I could see is 5, and the largest is 20.

Line 2:
This prints a random integer from the range [3, 10) with a step of 2.
The smallest number I could see is 3, and the largest is 9.
No, line 2 could not produce a 4 since the step is 2, and it would skip 4.

Line 3:
This prints a random floating-point number between 2.5 and 5.5.
The smallest number I could see is 2.5, and the largest is 5.5."""

"""
get random_number
display random_number
"""
random_number = random.randint(1, 100)
print(random_number)