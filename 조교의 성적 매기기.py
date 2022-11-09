T = int(input().rstrip())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(1, N + 1):
        rough_arr = list(map(int, input().split()))
        arr[i - 1].append((rough_arr[0] * 0.35 + rough_arr[1] * 0.45 + rough_arr[2] * 0.2))
        arr[i - 1].append(i)
    arr.sort(key=lambda x: x[0])
    idx = 0
    for i in range(N):
        if arr[i][1] == K:
            idx = i + 1
    if idx > 9 * N / 10:
        print("#" + str(t), "A+")
    elif idx > 8 * N / 10:
        print("#" + str(t), "A0")
    elif idx > 7 * N / 10:
        print("#" + str(t), "A-")
    elif idx > 6 * N / 10:
        print("#" + str(t), "B+")
    elif idx > 5 * N / 10:
        print("#" + str(t), "B0")
    elif idx > 4 * N / 10:
        print("#" + str(t), "B-")
    elif idx > 3 * N / 10:
        print("#" + str(t), "C+")
    elif idx > 2 * N / 10:
        print("#" + str(t), "C0")
    elif idx > 1 * N / 10:
        print("#" + str(t), "C-")
    elif idx > 0:
        print("#" + str(t), "D0")
