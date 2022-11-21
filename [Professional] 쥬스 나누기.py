T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append("1/" + str(N))
    print("#" + str(t), *arr)
