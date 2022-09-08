# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

from typing import List

# def missing_positive(num_array: List[int]) -> int:
#     result_array = [False] * (max(num_array) + 1)
#     for num in num_array:
#         if num >= 0:
#             result_array[num] = True
#         else:
#             continue
#     for i, result in enumerate(result_array):
#         if i != 0 and not result:
#             return i


def missing_positive1(num_array: List[int]) -> int:
    num_set = set(num_array)
    result = 1
    while result in num_set:
        result += 1
    return result


def missing_positive2(num_array: List[int]) -> int:
    if not num_array:
        return 1
    l = len(num_array)
    for i, num in enumerate(num_array):
        while i + 1 != num_array[i] and 0 < num_array[i] <= l:
            swap_index = num_array[i] - 1
            num_array[i], num_array[swap_index] = num_array[swap_index], num_array[i]
            if num_array[i] == num_array[swap_index]:
                break
    for i, num in enumerate(num_array, 1):
        if num != i:
            return i
    return l + 1


if __name__ == "__main__":
    num_array = [5, 6, 7, 8, 8, 9, 8, 10, 3, 4, -1, 1, 2]
    assert missing_positive2(num_array) == 11

# This is a good problem to use set because we need some kind of 'key' and we don't need to store value associated with it.
