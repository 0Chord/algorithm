T = int(input().rstrip())

for t in range(1, T + 1):
    arr = []
    for _ in range(5):
        arr.append(list(input().rstrip()))
    result_str = ""
    max_len = 0
    for el in arr:
        max_len = max(max_len, len(el))
    idx = 0
    while True:
        if idx == max_len:
            break
        for el in arr:
            if len(el) > idx:
                result_str += el[idx]
        idx += 1
    print("#" + str(t), result_str)
