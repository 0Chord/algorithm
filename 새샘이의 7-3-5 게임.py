def select_three(calc, count, idx):
    global three_arr
    if count == 3:
        if calc not in three_arr:
            three_arr.append(calc)
        return
    if idx == 7:
        return
    select_three(calc + tc_arr[idx], count + 1, idx + 1)
    select_three(calc, count, idx + 1)


T = int(input().rstrip())

for t in range(1, T + 1):
    tc_arr = list(map(int, input().split()))
    three_arr = []
    select_three(0, 0, 0)
    three_arr.sort()
    print("#" + str(t), three_arr[-5])
