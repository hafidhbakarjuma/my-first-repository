#!/usr/bin/python3
import random
number = 0

def check_number():
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")


if __name__ == "__main__":
    number = random.randint(-10, 10)
    check_number()