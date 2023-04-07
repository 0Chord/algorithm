def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    memo = [0] * (2001)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, 2001):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n] % 1234567
