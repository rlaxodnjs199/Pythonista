from typing import List


def arrayPairSum1(nums: List[int]):
    nums.sort()
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result


def arrayPairSum2(nums: List[int]):
    return sum(sorted(nums)[::2])


nums = [6, 2, 6, 5, 1, 2]
