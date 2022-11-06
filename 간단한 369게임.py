N = int(input())
arr = ["" for _ in range(N)]

for i in range(1, N + 1):
    str_num = str(i)
    for e in str_num:
        if int(e) % 3 == 0 and int(e) != 0:
            arr[i - 1] += "-"
for i in range(N):
    if arr[i] == '':
        arr[i] = i + 1
print(*arr)
