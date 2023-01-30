import sys

arr = list(map(int, list(sys.stdin.readline().rstrip())))
if len(arr) == 1:
    if arr[-1] == 0:
        print(0)
    else:
        print(1)
else:
    memo = [0] * len(arr)
    if arr[0] != 0:
        memo[0] = 1
    else:
        memo[0] = -1
    mini_tmp = str(arr[0]) + str(arr[1])

    if arr[1] == 0 and not (arr[0] == 1 or arr[0] == 2):
        memo[1] = -1
    elif memo[0] == -1:
        memo[1] = -1
    elif arr[1] == 0 and int(mini_tmp) <= 26:
        memo[1] = 1
    elif int(mini_tmp) > 26:
        memo[1] = 1
    elif int(mini_tmp) <= 26:
        memo[1] = 2

    for idx in range(2, len(arr)):
        tmp = str(arr[idx - 1]) + str(arr[idx])
        if memo[idx - 1] == -1:
            memo[idx] = -1
        elif arr[idx] == 0 and not (arr[idx - 1] == 1 or arr[idx - 1] == 2):
            memo[idx] = -1
        elif arr[idx] == 0 and arr[idx - 1] == 0:
            memo[idx] = -1
        elif arr[idx - 1] == 0:
            memo[idx] = memo[idx-1]
        elif arr[idx] == 0 or arr[idx - 1] == 0:
            memo[idx] = memo[idx - 2]
        elif int(tmp) > 26:
            memo[idx] = memo[idx - 1]
        elif int(tmp) <= 26:
            memo[idx] += memo[idx - 2]
            memo[idx] += memo[idx - 1]
    if memo[-1] == -1:
        print(0)
    else:
        print(memo[-1] % 1000000)
