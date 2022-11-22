T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    print("#" + str(t), N // 3)
