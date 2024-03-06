import sys

n = int(sys.stdin.readline().rstrip())

result = 0

for idx in range(1, n):
    numbers = list(map(int, list(str(idx))))
    if n == idx + sum(numbers):
        result = idx
        break
print(result)
