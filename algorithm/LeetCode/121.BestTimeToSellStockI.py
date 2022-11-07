from typing import List


def solution(prices: List[int]) -> int:
    min_price = prices[0]
    profit = float("-inf")
    for price in prices:
        local_profit = price - min_price
        profit = max(profit, local_profit)
        min_price = min(min_price, price)
    return profit


"""
Refactoring Technique
1. When you don't need to remember index, don't use range() to iterate list.
2. If you compare two values to update max, min, use max(), min() 
   instead of conditional statement.
"""
