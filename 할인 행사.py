from collections import Counter


def solution(want, number, discount):
    arr = {}
    for i in range(len(want)):
        arr[want[i]] = number[i]
    cnt = 0
    for i in range(len(discount) - 9):
        dic = dict(Counter(discount[i:i + 10]))
        flag = True
        for el in want:
            try:
                if arr[el] != dic[el]:
                    flag = False
                    break
            except:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt
