#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
#Last digit of 4205 is 5 and is less than 6 and not 0
num = str(number)
if num[-1:] > '5':
    #print goes here!
    print(f'Last digit of {number} is {str(number)[-1:]} and is greater than 5')
elif num[-1:] == '0':
        #Zero printing goes here!
    print(f'Last digit of {number} is {str(number)[-1:]} and is 0')
elif num[-1:] < '6':
    if num[-1:] != '0':
        #last print goes here! 
        print(f'Last digit of {number} is {str(number)[-1:]} and is less than 6 and not 0')
        