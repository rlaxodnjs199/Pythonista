from typing import List


def three_sum1(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                break
    return result


print(three_sum1([3, 0, -2, -1, 1, 2]))
