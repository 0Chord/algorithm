T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(input().split()))

    result_arr = ["" for _ in range(20)]

    idx = 0
    for el in arr:
        alphabet = el[0]
        count = int(el[1])
        for cnt in range(count):
            if len(result_arr[idx]) < 10:
                result_arr[idx] += alphabet
            elif len(result_arr[idx]) >= 10:
                idx += 1
                result_arr[idx] += alphabet
    print("#" + str(t))
    for el in result_arr:
        if el != "":
            print(el)
