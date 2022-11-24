T = int(input().rstrip())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    binary_M = str(bin(M))[2:]
    if len(binary_M) < N:
        binary_M = "0" * (N - len(binary_M)) + binary_M
    binary_M = binary_M[len(binary_M) - N:]
    flag = True
    for idx in range(N):
        if binary_M[idx] == "0":
            flag = False

    if flag:
        print("#" + str(t), "ON")
    else:
        print("#" + str(t), "OFF")
