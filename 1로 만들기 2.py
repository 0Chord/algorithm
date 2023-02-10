import sys

N = int(sys.stdin.readline().rstrip())
memo = [N] * (N + 1)
memo[1] = 0
lst_memo = [[idx] for idx in range(N + 1)]
for idx in range(1, N + 1):
    if idx * 3 < N + 1 and memo[idx] + 1 < memo[idx * 3]:
        memo[idx * 3] = memo[idx] + 1
        lst_memo[idx * 3] = lst_memo[idx][:]
        lst_memo[idx * 3].append(idx * 3)
    if idx * 2 < N + 1 and memo[idx] + 1 < memo[idx * 2]:
        memo[idx * 2] = memo[idx] + 1
        lst_memo[idx * 2] = lst_memo[idx][:]
        lst_memo[idx * 2].append(idx * 2)
    if idx + 1 < N + 1 and memo[idx] + 1 < memo[idx + 1]:
        memo[idx + 1] = memo[idx] + 1
        lst_memo[idx + 1] = lst_memo[idx][:]
        lst_memo[idx + 1].append(idx + 1)
print(memo[-1])
print(*lst_memo[-1][::-1])
