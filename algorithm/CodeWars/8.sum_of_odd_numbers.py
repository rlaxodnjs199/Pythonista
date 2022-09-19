# Problem
# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8


def row_sum_odd_numbers(n):
    result = 0
    odd = 1
    row_count = 1
    while n:
        if n != 1:
            temp_row_count = row_count
            while temp_row_count:
                odd += 2
                temp_row_count -= 1
            row_count += 1
            n -= 1
        else:
            while row_count:
                result += odd
                odd += 2
                row_count -= 1
            n -= 1
    return result
