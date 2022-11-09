T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().strip())
    result = 0
    for num in range(1, N + 1):
        if num % 2 == 1:
            result += num
        else:
            result -= num
    print("#" + str(t), result)
