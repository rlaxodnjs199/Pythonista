# Problem
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example
# The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits1(n):
    return bin(n)[2:].count('1')


def countBits2(n):
    total_1 = 0
    while n > 0:
        # n & 1 equals to n % 2 but faster
        last_digit_bit = n & 1
        total_1 += last_digit_bit
        n >>= 1
    return total_1
