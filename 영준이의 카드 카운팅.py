T = int(input().rstrip())

for t in range(1, T + 1):
    rough_str = input().rstrip()
    arr = []
    for idx in range(0, len(rough_str), 3):
        arr.append(rough_str[idx:idx + 3])
    count_arr = [13] * 4
    lst = []
    flag = True
    for el in arr:
        if el in lst:
            flag = False
            break
        else:
            lst.append(el)
            if el[0] == 'S':
                count_arr[0] -= 1
            elif el[0] == 'D':
                count_arr[1] -= 1
            elif el[0] == 'H':
                count_arr[2] -= 1
            elif el[0] == 'C':
                count_arr[3] -= 1

    if flag:
        print("#"+str(t), *count_arr)
    else:
        print("#"+str(t), "ERROR")
