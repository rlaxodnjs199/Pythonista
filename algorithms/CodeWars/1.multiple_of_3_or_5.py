def solution(number):
    if number < 0:
        return 0

    list_3 = []
    list_5 = []
    list_15 = []
    x_3 = 3
    x_5 = 5
    x_15 = 15

    while x_3 < number:
        list_3.append(x_3)
        x_3 += 3
    while x_5 < number:
        list_5.append(x_5)
        x_5 += 5
    while x_15 < number:
        list_15.append(x_15)
        x_15 += 15

    return sum(list_3) + sum(list_5) - sum(list_15)
