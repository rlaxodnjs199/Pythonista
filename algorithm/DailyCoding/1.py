# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def twosum(num_list, k):
    num_seen = set()
    for num in num_list:
        if k - num in num_seen:
            return True
        num_seen.add(num)
    return False


# Comment
# Dictionary and Set are two different type.
# Use Dictionary when you need to store hashed keys with their corresponding values.
# Time: O(n), Space: O(n)


def twosum2(num_list, k):
    num_list.sort()
    p1 = 0
    p2 = len(num_list) - 1
    while p1 != p2:
        sum = num_list[p1] + num_list[p2]
        if sum == k:
            return True
        elif sum < k:
            p1 += 1
        else:
            p2 -= 1
    return False


# Comment
# Sort the list first, then iterate the array with two pointers, one at the start and one at the end.
# Time: O(n log n), Space: O(1)

if __name__ == "__main__":
    print(twosum2([10, 15, 3, 7], 11))
