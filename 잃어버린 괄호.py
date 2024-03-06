import sys

arr = list(sys.stdin.readline().rstrip().split("-"))
result = 0
for idx in range(len(arr)):
    numbers = list(map(int, arr[idx].split("+")))
    cnt = 0
    for number in numbers:
        cnt += number
    if idx == 0:
        result += cnt
    else:
        result -= cnt

print(result)
