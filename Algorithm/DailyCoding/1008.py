# This problem was asked by Salesforce.
# Given an array of integers, find the maximum XOR of any two elements.
from typing import List

def solution(narray: List[int]) -> int:
	max_xor = 0
	for idx1, n1 in enumerate(narray):
		for n2 in narray[idx1+1:]:
			if (n1 << n2) > max_xor:
				max_xor = n1 << n2
	return max_xor 

if __name__ == '__main__':
	narray = [1,2,3]
	print(solution(narray))

# Today I learned:
# How to iterate multiple for-loop with different start index?
# 1. Use range
#   for i in range(0, len(narray)):
# 		for j in range(i+1, len(narray)):
# 			print(narray[i], narray[j])
# 2. Use enumerate
# 	for idx1, n1 in enumerate(narray):
# 		for n2 in narray[idx1+1:]:
# 			print(n1, n2)