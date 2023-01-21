L, C = map(int, input().rstrip().split())

arr = list(input().rstrip().split())
result_arr = []

vowel_arr = ['a', 'e', 'i', 'o', 'u']


def recur(idx, string):
    if idx == C:
        return
    string += arr[idx]

    if len(string) == L:
        flag = False
        count = L
        sorted_arr = sorted(string)
        for el in sorted_arr:
            if el in vowel_arr:
                flag = True
                count -= 1
        sorted_str = "".join(s for s in sorted_arr)

        if sorted_str not in result_arr and flag and count >= 2:
            result_arr.append(sorted_str)
    recur(idx + 1, string)
    recur(idx + 1, string[:-1])


recur(0, "")
result_sorted = sorted(result_arr)
for el in result_sorted:
    print(el)
