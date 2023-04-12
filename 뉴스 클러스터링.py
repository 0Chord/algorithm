from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    for i in range(len(str1) - 1):
        slice_str = str1[i:i + 2]
        if 97 <= ord(slice_str[0]) <= 122 and 97 <= ord(slice_str[1]) <= 122:
            s1.append(slice_str)
    for i in range(len(str2) - 1):
        slice_str = str2[i:i + 2]
        if 97 <= ord(slice_str[0]) <= 122 and 97 <= ord(slice_str[1]) <= 122:
            s2.append(slice_str)

    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    s1_set = list((counter_s1 & counter_s2).elements())
    s2_set = list((counter_s1 | counter_s2).elements())

    if len(s1_set) == 0 and len(s2_set) == 0:
        return 65536
    else:
        return int(len(s1_set) / len(s2_set) * 65536)
