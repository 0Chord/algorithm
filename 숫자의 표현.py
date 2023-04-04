def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        sum = 0
        num = i
        while True:
            if sum >= n:
                break
            sum += num
            num += 1
        if sum == n:
            cnt += 1
    answer = 0
    return cnt
