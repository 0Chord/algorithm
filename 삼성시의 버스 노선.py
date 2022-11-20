T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    P = int(input().rstrip())
    c_arr = []

    for _ in range(P):
        c_arr.append(int(input().rstrip()))
    count_list = [0 for _ in range(5000)]
    for el in arr:
        for idx in range(el[0], el[1] + 1):
            count_list[idx - 1] += 1
    result_list = []
    for el in c_arr:
        result_list.append(count_list[el - 1])
    print("#" + str(t), *result_list)
