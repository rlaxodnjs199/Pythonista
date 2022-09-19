"""
49. Group Anagrams
"""
import collections
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[("").join(sorted(word))].append(word)

    return anagrams.values()
