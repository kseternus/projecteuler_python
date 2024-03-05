# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 / 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
for i in range(1, 999):
    for j in range(1, 999):
        result = i * j
        string = str(result)
        rev_string = string[::-1]
        if string == rev_string:
            palindromes.append(int(string))

palindromes.sort()
print(palindromes[-1])
