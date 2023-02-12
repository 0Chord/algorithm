import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
start = 0
end = max(arr)
max_len = 0

while start <= end:
    count = 0
    mid = (start + end) // 2
    if end == 1:
        mid = 1
    for el in arr:
        if el >= mid:
            count += el // mid
    if count >= N:
        max_len = mid
        start = mid + 1
    else:
        end = mid - 1
print(max_len)
