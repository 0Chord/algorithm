import sys

d, k = map(int, sys.stdin.readline().rstrip().split())
day1 = 1
day2 = 1
while True:
    memo = [0] * 31
    memo[1] = day1
    memo[2] = day2
    for day in range(3, d + 1):
        memo[day] = memo[day - 1] + memo[day - 2]
    if memo[d] < k:
        day2 += 1
    elif memo[d] > k:
        day1 += 1
        day2 = day1
    else:
        print(day1)
        print(day2)
        break
