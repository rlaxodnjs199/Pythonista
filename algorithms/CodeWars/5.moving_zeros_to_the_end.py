# Problem
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
def move_zeros1(arr):
    zeros = []
    non_zeros = []
    # Append single element to the list: use += or append
    for n in arr:
        if n == 0:
            zeros.append(n)
        else:
            non_zeros.append(n)
    # Concatenate list to the list: use extend
    return non_zeros.extend(zeros)


def move_zeros2(arr):
    # element of an array can be any value.
    # If element is False, we should not treat this as 0.
    non_zeros = [el for el in arr if isinstance(el, bool) or el != 0]
    return non_zeros + [0] * (len(arr) - len(non_zeros))
