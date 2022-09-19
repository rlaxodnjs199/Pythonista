# Custom generator using the generator pattern
class iterator_n(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        raise StopIteration()


# Generator function using yield expression
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# Print memory usage of objects
import sys

nums_squared_lc = [i ** 2 for i in range(10000)]
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_lc))
print(sys.getsizeof(nums_squared_gc))

# Print performance of operations
import cProfile

cProfile.run("sum(nums_squared_lc)")
cProfile.run("sum(nums_squared_gc)")

# Detect palindrome number
def is_palindrome(num):
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


import math

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = int(math.log(i, 10)) + 1
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
