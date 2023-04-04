def solution(n):
    num = str(bin(n))[2:]
    arr = [0, 0]
    for el in num:
        if el == '0':
            arr[0] += 1
        elif el == '1':
            arr[1] += 1
    while True:
        n += 1
        one_cnt = 0
        num = str(bin(n))[2:]
        for el in num:
            if el == '1':
                one_cnt += 1
        if one_cnt == arr[1]:
            break
    return n
