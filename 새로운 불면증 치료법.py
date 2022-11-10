T = int(input().rstrip())

for t in range(1, T + 1):
    arr = [0 for _ in range(10)]
    N = int(input().rstrip())
    count = N
    while True:
        N_str = str(N)
        for el in N_str:
            arr[int(el)] += 1
        flag = True
        for el in arr:
            if el == 0:
                flag = False
        if flag:
            break
        N += count
    print("#" + str(t), N)
