import random

number = random.randint(-10, 10)

#my code goes here

if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
