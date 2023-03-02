import sys
import math

n = int(sys.stdin.readline().rstrip())


def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


INF = int(1e10)
for idx in range(n, INF):
    flag = True
    for el in range(len(str(idx)) // 2):
        if str(idx)[el] != str(idx)[len(str(idx)) - 1 - el]:
            flag = False
    if flag:
        if check_prime(idx):
            print(idx)
            break
