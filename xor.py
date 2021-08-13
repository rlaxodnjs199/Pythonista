n = 3
x = 3
y = 4

for _ in range(10):
	n ^= (x ^ y)
	print(n)

def swap_without_variable(a, b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return a, b

if __name__ == '__main__':
	print(swap_without_variable(3,5))