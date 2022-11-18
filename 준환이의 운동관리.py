T = int(input().rstrip())

for t in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X > U:
        print("#" + str(t), -1)
    elif U >= X >= L:
        print("#" + str(t), 0)
    else:
        print("#" + str(t), L - X)
