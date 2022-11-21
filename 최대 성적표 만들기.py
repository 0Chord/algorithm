T = int(input().rstrip())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    result = 0
    for idx in range(K):
        result += arr[idx]
    print("#" + str(t), result)
