import sys

k = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))
