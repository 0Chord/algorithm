T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    average = 0
    for _ in range(N):
        p, x = map(float, input().split())
        average += p * x
    print("#" + str(t), "{:.6f}".format(average))
