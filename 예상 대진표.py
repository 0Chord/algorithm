import math
def solution(n,a,b):
    answer = 0
    cnt = 0
    while True:
        if (a + 1 == b and b%2 == 0) or (b+1 == a and a%2 == 0):
            cnt += 1
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        cnt += 1
    return cnt