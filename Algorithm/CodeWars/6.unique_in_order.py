# Problem
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# Example
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order1(iterable):
    if len(iterable) == 0:
        return []
    if len(iterable) == 1:
        return [iterable]
    result = []
    for index, item in enumerate(iterable):
        if index == 0:
            continue
        if item != iterable[index-1]:
            result.append(item)
    return result


def unique_in_order2(iterable):
    result = []
    prev = None
    for item in iterable:
        if item != prev:
            result.append(item)
    return result

# Comment
# 1. It is wise to store information in 'prev' variable and update it other than reading item from iterable[index-1].
# 2. By setting 'prev' to None, we can escape the issue when length of iterable is less than 2.
#    If iterable length == 0: don't go over looping
#    If iterable length == 1: compare iterable[0] with prev.
