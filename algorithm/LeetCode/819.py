# Most Common Word
import collections
import re
from typing import Dict

PARAGRAPH = "Bob hit a ball, the hit BALL flew far after it was hit."
BANNED = ["hit"]


def most_common_word(p: str, banned: Dict):
    words = [
        word for word in re.sub(r"[^\w]", " ", p).lower().split() if word not in banned
    ]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


print(most_common_word(PARAGRAPH, BANNED))
