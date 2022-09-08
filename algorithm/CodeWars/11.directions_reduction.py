def dirReduc(arr):
    if len(arr) <= 1:
        return arr
    dir_labels = {'NORTH': 1, 'SOUTH': -1, 'EAST': 2, 'WEST': -2}
    result = [arr[0]]
    for dir in arr[1:]:
        if len(result) > 0 and dir_labels[result[-1].upper()] + dir_labels[dir.upper()] == 0:
            result.pop()
        else:
            result.append(dir)
    return result

# Things I learned
# Use dictionary to use specific values as variables
# list.pop(index) & list.append(element)
