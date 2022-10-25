from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if nums_map.get(complement):
            return [nums_map[complement], i]
        nums_map[num] = i
