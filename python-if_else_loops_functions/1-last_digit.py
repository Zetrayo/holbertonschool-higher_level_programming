#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = - number % 10
    digit = - digit
else:
    digit = number % 10
if digit < 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit < 6 and digit > 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
