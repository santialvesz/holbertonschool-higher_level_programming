#!/usr/bin/python3
import random
number = 1007
number1 = 100
number2 = -98
last_digit = number % 10
last_digit1 = number1 % 10
last_digit2 = abs(number2) % 10 * -1


if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")

if last_digit1 == 0:
    print(f"Last digit of {number1} is {last_digit1} and is 0")

if (last_digit2 < 6) and (last_digit != 0):
    print(f"Last digit of {number2} is {last_digit2} and is less than 6 and its no 0")
