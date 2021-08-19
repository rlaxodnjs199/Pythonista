# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
from typing import List

def canPartition(self, nums: List[int]) -> bool:
	target, n = sum(nums), len(nums)
	if target == 0:
		return False
	target >>= 1
	dp = [True] + [False]*target
	for num in nums:
		dp = [dp[s] or (s >= num and dp[s-num]) for s in range(target+1)]
		if dp[target]:
			return True
	return False