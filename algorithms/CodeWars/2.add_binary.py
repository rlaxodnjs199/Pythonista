def add_binary_1(a, b):
    # bin() starts with prefix [0b]
    return bin(a+b)[2:]


def add_binary_2(a, b):
    target = a+b
    mul_2 = 1
    # stop updating the variable right after reaching the target
    while (mul_2 * 2 <= target):
        mul_2 *= 2

    # integer division: //
    binary_str = ''
    while mul_2 > 0:
        if target >= mul_2:
            target -= mul_2
            mul_2 //= 2
            binary_str += '1'
        else:
            mul_2 //= 2
            binary_str += '0'

    return binary_str
