# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def num_encodings(s):
	def helper(s):
		if s.startswith('0'):
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


if __name__ == '__main__':
	print(num_encodings('1111111111'))