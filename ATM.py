import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
cnt = 0
result = 0
for el in arr:
    cnt += el
    result += cnt
print(result)
