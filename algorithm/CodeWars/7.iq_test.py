# Problem
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# Examples
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

def iq_test1(numbers):
    last_even_index = 0
    last_odd_index = 0
    even_count = 0
    odd_count = 0
    numbers = numbers.split(' ')
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            odd_count += 1
            last_odd_index = i+1
            if even_count != 0 and even_count > odd_count:
                return last_even_index
        else:
            even_count += 1
            last_even_index = i + 1
            if odd_count != 0 and odd_count > even_count:
                return last_odd_index
    return len(numbers)


def iq_test2(numbers):
    even_odd_list = [int(n) % 2 == 0 for n in numbers.split(' ')]
    return even_odd_list.index(True)+1 if even_odd_list.count(True) == 1 else even_odd_list.index(False)

# Comment
# Make bool list of even & odd then return result with list.index & list.count.
# Even though the performance is not optimal, solution 2 has same time complexity in terms of Big O notation(O(2n) vs O(4n))
