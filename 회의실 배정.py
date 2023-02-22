import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]

for idx in range(1, len(arr)):
    if end_time <= arr[idx][0]:
        cnt += 1
        end_time = arr[idx][1]

print(cnt)