import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number < 0:
    print(str(number) + '  Is negative')
elif number == 0:
    print(str(number) + '  Is Zero')
elif number > 0:
    print(str(number) + '  Is positive')
