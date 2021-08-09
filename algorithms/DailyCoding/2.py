# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

from typing import List

def solution(num_array: List[int]) -> List[int]:
	mul = 1
	for num in num_array:
		mul *= num
	return [int(mul/n) for n in num_array]

if __name__ == '__main__':
	num_array = [1,2,3,4,5]
	print(solution(num_array))
