# Functions to evaluate the FizzBuzz problem


def fizzbuzz(number):
    divisible_by_three = (number % 3) == 0
    divisible_by_five = (number % 5) == 0

    if divisible_by_five and divisible_by_three:
        return "FizzBuzz"

    if divisible_by_three:
        return "Fizz"

    if divisible_by_five:
        return "Buzz"

    return number
