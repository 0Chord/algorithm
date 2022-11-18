T = int(input().rstrip())

for t in range(1, T + 1):
    f_h, f_m, s_h, s_m = map(int, input().split())
    hour = 0
    minute = 0
    if f_m + s_m >= 60:
        minute = f_m + s_m - 60
        hour += 1
    else:
        minute = f_m + s_m

    if hour + f_h + s_h > 12:
        hour = hour + f_h + s_h - 12
    else:
        hour = hour + f_h + s_h
    print("#" + str(t), hour, minute)
