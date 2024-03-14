# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean():
    abc_product = 0
    for a in range(1, 499+1):
        for b in range(1, 499+1):
            c = 1000 - b - a
            if a*a + b*b == c*c:
                abc_product = a*b*c
    return abc_product


print(pythagorean())
