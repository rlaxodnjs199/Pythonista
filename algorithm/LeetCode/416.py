# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
from typing import List


def canPartition(self, nums: List[int]) -> bool:
    target, n = sum(nums), len(nums)
    if target == 0:
        return False
    target >>= 1
    dp = [True] + [False] * target
    for num in nums:
        dp = [dp[s] or (s >= num and dp[s - num]) for s in range(target + 1)]
        if dp[target]:
            return True
    return False


def canPartition2(self, nums: List[int]) -> bool:
    s = sum(nums)
    if s & 1:
        return False

    def helper(self, nums, target, ind, n, d):
        if target in d:
            return d[target]
        if target == 0:
            d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if helper(nums, target - nums[i], i + 1, n, d):
                        d[target] = True
                        break
        return d[target]

    return helper(nums, s >> 1, 0, len(nums), {})
