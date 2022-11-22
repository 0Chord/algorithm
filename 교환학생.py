import math

T = int(input().rstrip())

for t in range(1, T + 1):
    n = int(input().rstrip())
    arr = list(map(int, input().split()))

    day_count = math.inf

    for idx in range(len(arr)):
        calc_str = ""
        for i in range(idx, len(arr)):
            calc_str += str(arr[i])
        for i in range(0, idx):
            calc_str += str(arr[i])
        calc_arr = list(map(int,list(calc_str)))
        mini_day_count = 0
        calc_n = n
        while True:
            if calc_n == 0:
                break
            for i in range(len(calc_arr)):
                if calc_arr[i] == 1:
                    calc_n -= 1
                mini_day_count += 1
                if calc_n == 0:
                    break
        day_count = min(day_count, mini_day_count)
    print("#" + str(t), day_count)
