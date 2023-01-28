import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
broken_button_arr = []
if M != 0:
    broken_button_arr = list(map(int, sys.stdin.readline().rstrip().split()))
button_arr = [True] * 10
for el in broken_button_arr:
    button_arr[el] = False
min_count = abs(N-100)

arr = []
for idx in range(N * 2 + 10):
    flag = True
    for el in broken_button_arr:
        if str(el) in list(str(idx)):
            flag = False
            break
    if flag:
        arr.append(idx)

for el in arr:
    min_count = min(min_count, abs(N - el) + len(str(el)), abs(N - 100))
print(min_count)
