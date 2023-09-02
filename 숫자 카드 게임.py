import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    lst.sort()
    arr.append(lst)
idx = 0
max_num = -1
for index in range(len(arr)):
    if arr[index][0] > max_num:
        idx = index
        max_num = arr[index][0]
print(max_num)


