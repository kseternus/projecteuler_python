# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million.
import math

primes = []
number = 2
while number < 2000000+1:
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            break
    else:
        print(number)
        primes.append(number)
    number += 1

print(sum(primes))

