from typing import List


def productExceptSelf(nums: List[int]):
    output = []
    p = 1
    for i in range(len(nums)):
        output.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= p
        p *= nums[i]
    return output
