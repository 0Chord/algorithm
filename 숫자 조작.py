T = int(input().rstrip())

for t in range(1, T + 1):
    N = list(input().rstrip())
    max_num = int("".join(N))
    min_num = int("".join(N))

    flag_arr = [False] * len(N)
    for idx in range(len(N) - 1):
        for change_idx in range(idx + 1, len(N)):
            tmp = N[idx]
            N[idx] = N[change_idx]
            N[change_idx] = tmp
            max_num = max(max_num, int("".join(N)))
            tmp = N[idx]
            N[idx] = N[change_idx]
            N[change_idx] = tmp

        for change_idx in range(idx + 1, len(N)):
            if idx == 0 and N[change_idx] != "0":
                tmp = N[idx]
                N[idx] = N[change_idx]
                N[change_idx] = tmp
                min_num = min(min_num, int("".join(N)))
                tmp = N[idx]
                N[idx] = N[change_idx]
                N[change_idx] = tmp
            elif idx != 0:
                tmp = N[idx]
                N[idx] = N[change_idx]
                N[change_idx] = tmp
                min_num = min(min_num, int("".join(N)))
                tmp = N[idx]
                N[idx] = N[change_idx]
                N[change_idx] = tmp

    print("#" + str(t), min_num, max_num)
