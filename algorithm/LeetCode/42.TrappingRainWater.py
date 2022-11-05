from collections import deque
from typing import List


def trap(height: List[int]) -> int:
    l_index, r_index = 0, len(height) - 1
    l_max, r_max = height[l_index], height[r_index]
    total_water = 0

    while l_index < r_index:
        l_max = max(l_max, height[l_index])
        r_max = max(r_max, height[r_index])

        if l_max <= r_max:
            total_water += l_max - height[l_index]
            l_index += 1
        else:
            total_water += r_max - height[r_index]
            r_index -= 1

    return total_water


def trap2(height: List[int]) -> int:
    stack = deque()
    total_water = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            total_water += water * distance

        stack.append(i)

    return total_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert trap2(height) == 6
