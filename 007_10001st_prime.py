# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10,001st prime number?
import math


def given_prime_number(given):
    counter = 0
    number = 2
    while counter < given:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                break
        else:
            print(number)
            counter += 1
        number += 1


given_prime_number(10001)

