T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = list(map(int, input().split()))
    flag = False
    max_num = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            mini_flag = True
            str_num = str(arr[i] * arr[j])
            for idx in range(len(str_num) - 1):
                if str_num[idx] > str_num[idx + 1]:
                    mini_flag = False
                    break
            if mini_flag:
                flag = True
                max_num = max(max_num, int(str_num))
    if flag:
        print("#" + str(t), max_num)
    else:
        print("#" + str(t), -1)
