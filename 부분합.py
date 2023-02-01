import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0
min_length = N + 1
left, right = 0, 0

while True:
    if sum >= S:
        min_length = min(min_length, right - left)
        sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum += arr[right]
        right += 1
if min_length == N + 1:
    print(0)
else:
    print(min_length)
