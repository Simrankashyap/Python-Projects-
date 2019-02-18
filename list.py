# Implements a list of unique numbers

import get_int


numbers = []


while True:


    number = get_int("number: ")

    if not number:
        break


    if number not in numbers:

        numbers.append(number)

print()
for number in numbers:
    print(number)
