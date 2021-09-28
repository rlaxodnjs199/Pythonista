# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


def num_encodings(s):
    def helper(s):
        if s.startswith("0"):
            return 0
        if len(s) <= 1:
            return 1
        count = 0
        if int(s[:2]) <= 26:
            count += helper(s[2:])
        count += helper(s[1:])
        return count

    total = helper(s)
    return total


def num_encodings_dp(s):
    cache = {}
    cache[len(s)] = 1

    for i in reversed(range(len(s))):
        if s[i].startswith("0"):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i : i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]


if __name__ == "__main__":
    print(num_encodings_dp("1111111111"))
    print(num_encodings_dp("11"))
    print(num_encodings_dp("10"))
    print(num_encodings_dp("10101010"))
