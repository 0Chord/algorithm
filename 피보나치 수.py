def solution(n):
    memo = [0] * 100001
    memo[0] = 0
    memo[1] = 1
    for idx in range(2, 100001):
        memo[idx] = memo[idx - 1] + memo[idx - 2]

    return memo[n] % 1234567