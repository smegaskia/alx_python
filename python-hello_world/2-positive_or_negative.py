import random

number = random.randint(-10, 10)

# Your code here

if number < 0:
    print(f"{number} Is negative")
elif number == 0:
    print(f"{number} Is Zero")
elif number > 0:
    print(f"{number} is positive")
