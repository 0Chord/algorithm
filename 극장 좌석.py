import sys

n = int(sys.stdin.readline().rstrip())

move_arr = []

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    move_arr.append(int(sys.stdin.readline().rstrip()))

calc = 1
num_arr = [1, 1, 2]

for idx in range(3, 41):
    num_arr.append(num_arr[idx - 1] + num_arr[idx - 2])

move_arr.sort()

ans = 1
if m >= 1:
    tmp = 0
    for i in range(m):
        ans *= num_arr[move_arr[i] - 1 - tmp]
        tmp = move_arr[i]
    ans *= num_arr[n - tmp]
else:
    ans = num_arr[n]
print(ans)
