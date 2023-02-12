import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
start = 0
end = max(arr)
max_height = 0
while start <= end:
    slice_sum = 0
    mid = (start + end) // 2
    for el in arr:
        if el - mid >= 0:
            slice_sum += el - mid
    if slice_sum >= M:
        max_height = mid
        start = mid + 1
    else:
        end = mid - 1
print(max_height)
