T = int(input().strip())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))

    max_num = 0
    count_sum = 0
    if len(N) == len(M):
        for idx in range(len(N)):
            count_sum += N[idx] * M[idx]
        max_num = max(max_num, count_sum)
    elif len(N) < len(M):
        for idx in range(len(M) - len(N) + 1):
            count_sum = 0
            for mini_idx in range(len(N)):
                count_sum += N[mini_idx] * M[idx + mini_idx]
            max_num = max(max_num, count_sum)
    elif len(N) > len(M):
        for idx in range(len(N) - len(M) + 1):
            count_sum = 0
            for mini_idx in range(len(M)):
                count_sum += N[idx + mini_idx] * M[mini_idx]
            max_num = max(max_num, count_sum)
    print("#" + str(t), max_num)
