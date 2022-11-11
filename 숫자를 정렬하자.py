T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = list(map(int, input().split()))
    arr.sort()
    print("#" + str(t), *arr)
