def reverseStr(s: str, k: int):
    s_list = list(s)
    for i in range(0, len(s_list), 2 * k):
        s_list[i : i + k] = s_list[i : i + k][::-1]

    return "".join(s_list)


print(reverseStr("abcdefg", 2))
