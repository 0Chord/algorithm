import math


def solution(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = rev_base[::-1]
    pr_str = ""
    cnt = 0
    for idx in range(len(rev_base)):
        if rev_base[idx] == '0':
            if pr_str != '':
                pr = int(pr_str)
                if decision_prim(pr):
                    cnt += 1
                pr_str = ""
        else:
            pr_str += rev_base[idx]
            if idx == len(rev_base) - 1:
                if pr_str != '':
                    pr = int(pr_str)
                    if decision_prim(pr):
                        cnt += 1
    return cnt


def decision_prim(n: int):
    if n == 1:
        return False
    elif n >= 2:
        flag = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        if flag:
            return True
