# This problem was asked by Salesforce.
# Given an array of integers, find the maximum XOR of any two elements.
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self, size: int) -> None:
        self.root = TrieNode()
        self.size = size

    def insert(self, n: int) -> None:
        p = self.root

        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            if bit not in p.children:
                p.children[bit] = TrieNode()
            p = p.children[bit]

    def find_max_xor(self, n: int):
        p = self.root
        max_xor = 0
        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            if (1 - bit) in p.children:
                max_xor |= 1 << i
                p = p.children[not bit]
            else:
                p = p.children[bit]

        return max_xor


def solution(narray: List[int]) -> int:
    size = max(narray).bit_length()
    trie = Trie(size)

    for n in narray:
        trie.insert(n)

    max_xor = 0
    for n in narray:
        max_xor = max(max_xor, trie.find_max_xor(n))

    return max_xor


if __name__ == "__main__":
    print(solution([4, 6, 7, 2]))


# Today I learned:
# How to iterate multiple for-loop with different start index?
# 1. Use range
#   for i in range(0, len(narray)):
# 		for j in range(i+1, len(narray)):
# 			print(narray[i], narray[j])
# 2. Use enumerate
# 	for idx1, n1 in enumerate(narray):
# 		for n2 in narray[idx1+1:]:
# 			print(n1, n2)
#
# Bit operation '~' doesn't work as I expected"
# 	The most significant bit is a sign bit, so flipping the entire bit
#	throws different result compare to (1 - bit)
# Insert to Trie structure: O(k * N) where k is a max bit length and N is a number of elements in the array.
# Find maximum xor: O(k * N) as well since the depth of the tree is k.