T = int(input().rstrip())

for t in range(1, T + 1):
    m, d = map(int, input().split())
    days = 0
    if m > 1:
        for month in range(2, m + 1):
            if month == 3:
                days += 29
            elif month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
                days += 31
            elif month == 5 or month == 7 or month == 10 or month == 12:
                days += 30
    days += d
    arr = [3, 4, 5, 6, 0, 1, 2]
    print("#" + str(t), arr[days % 7])
