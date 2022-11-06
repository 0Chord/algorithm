import sys

for k in range(10):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(2, N - 2):
        calc = 0
        max_num = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if max_num >= arr[i]:
            result += 0
        else:
            result += (arr[i] - max_num)
    print("#" + str((k + 1)), str(result))
