def func_prefix(sub_str):
    sub_len = len(sub_str)
    prefix_array = [0]*sub_len
    i, j = 0, 1
    while j < sub_len:
        if sub_str[i] == sub_str[j]:
            prefix_array[j] = i + 1
            i += 1
            j += 1

        elif i:
            i = prefix_array[i - 1]
        else:
            prefix_array[j] = 0
            j += 1
    return prefix_array


def kmp(sub_str, text_str=""):
    sub_len = len(sub_str)
    text_len = len(text_str)
    if not text_len or sub_len > text_len:
        return []
    prefix_array = func_prefix(sub_str)
    print(">>>", prefix_array)
    result = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text_str[i] == sub_str[j]:
            if j == sub_len - 1:
                result.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1

        elif j:
            j = prefix_array[j-1]
        else:
            i += 1
    return result

# if __name__ == '__main__':
#     s = "abcabeabcabcabdrabcabdtuyeabcabdwrt"
#     sub = "abcabd"
#     P = kmp(s, sub)
#     print(P)
#     # for i in P:
#     #     print(s[i:i + len(sub)])