# Transpose matrix

def transpose1(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for item in matrix:
            row.append(item[i])
        result.append(row)
    return result


def transpose2(matrix):
    result = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return result


if __name__ == '__main__':
    matrix = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
    print(transpose2(matrix))
