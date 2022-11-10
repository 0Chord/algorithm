def recur(N, M, n):
    if M == 1:
        return N
    else:
        return recur(N * n, M - 1, n)


for t in range(1, 11):
    test_case = input().rstrip()
    N, M = map(int, input().split())

    print("#"+str(t),recur(N, M, N))
