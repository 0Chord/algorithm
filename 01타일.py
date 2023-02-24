import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] * (n + 1)
for idx in range(1, n + 1):
    if idx == 1:
        arr[idx] = 1
    elif idx == 2:
        arr[idx] = 2
    else:
        arr[idx] = arr[idx - 1] % 15746 + arr[idx - 2] % 15746

print(arr[n] % 15746)
