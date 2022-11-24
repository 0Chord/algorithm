T = int(input().rstrip())
month_arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(1, T + 1):
    f_m, f_d, s_m, s_d = map(int, input().split())
    days = 0
    if f_m == s_m:
        days += s_d - f_d + 1
    else:
        days += month_arr[f_m] - f_d + 1
        days += s_d
        if f_m + 1 < s_m:
            for month in range(f_m + 1, s_m):
                days += month_arr[month]
    print("#"+str(t),days)